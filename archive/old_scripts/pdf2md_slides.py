#!/usr/bin/env python3
"""
pdf2md_slides_rtl.py
PDF (slides/presentations) -> Markdown with robust Hebrew RTL fixes.

Install:
  python3 -m pip install pymupdf python-bidi regex

Run:
  python3 pdf2md_slides_rtl.py
  # optional:
  python3 pdf2md_slides_rtl.py --pdf "file.pdf" --out "file.md"
"""

import argparse
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF
import regex as reg

try:
    from bidi.algorithm import get_display
except Exception:
    get_display = None

HEBREW_RE = reg.compile(r"[\p{Hebrew}]")
HEBREW_WORD_RE = reg.compile(r"\p{Hebrew}+")
LATIN_RUN_RE = re.compile(r"[A-Za-z]{3,}")  # 3+ letters run

WHITESPACE_RE = re.compile(r"[ \t]+")
SOFT_HYPHENS = ["\u00ad", "\u200e", "\u200f", "\ufeff"]


# A small but effective Hebrew lexicon for scoring (general + product/research slide vocabulary).
HE_COMMON = {
    "של", "עם", "על", "אל", "זה", "זאת", "יש", "אין", "מה", "איך", "למה", "כי", "לא", "כן",
    "את", "האם", "אנחנו", "אתם", "אתן", "אני", "הוא", "היא", "הם", "הן", "כמו", "גם",
    "יותר", "פחות", "כדי", "לפני", "אחרי", "בין", "בתוך", "נגד", "מול",
    "מוצר", "ניהול", "מחקר", "שוק", "ניתוח", "מתחרים", "מצגת", "סטודנטים", "שאלה", "שאלות",
    "קהל", "קהלי", "מטרה", "הבעיה", "פתרון", "משתמשים", "משתמש", "לקוחות", "לקוח",
    "נתונים", "תובנות", "תחרות", "סיכונים", "פיתוח", "אפליקציה", "רעיונות", "רעיון",
    "כמותי", "איכותי", "ראשוני", "משני", "סקר", "ראיונות", "ראיון",
}

LATIN_KEEP = {"TAM", "SAM", "SOM", "MVP", "AI", "API", "UX", "UI"}


def contains_hebrew(s: str) -> bool:
    return bool(HEBREW_RE.search(s))


def cleanup_line(s: str) -> str:
    for ch in SOFT_HYPHENS:
        s = s.replace(ch, "")
    s = WHITESPACE_RE.sub(" ", s)
    return s.strip()


def extract_page_lines(page: fitz.Page) -> list[str]:
    """
    More stable than get_text("text") for slides:
    read blocks sorted top->bottom, left->right, then split into lines.
    """
    blocks = page.get_text("blocks")
    text_blocks = [(b[0], b[1], b[4]) for b in blocks if isinstance(b[4], str) and b[4].strip()]
    text_blocks.sort(key=lambda t: (round(t[1], 1), round(t[0], 1)))

    lines = []
    for _, _, t in text_blocks:
        for raw in t.splitlines():
            raw = raw.rstrip()
            if raw.strip():
                lines.append(raw)
    return lines


def looks_bad_leading_punct(s: str) -> bool:
    return bool(s) and s[0] in ":;,.?!)]}»"


def reverse_words_preserving_spaces(s: str) -> str:
    parts = s.split()
    return " ".join(parts[::-1])


def reverse_hebrew_tokens_only(s: str) -> str:
    """
    Reverse only Hebrew word tokens (characters), keep non-Hebrew segments as-is.
    Useful when PDF stored Hebrew glyphs reversed but Latin/nums are fine.
    """
    out = []
    i = 0
    while i < len(s):
        m = HEBREW_WORD_RE.match(s, i)
        if m:
            out.append(m.group(0)[::-1])
            i = m.end()
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def hebrew_word_hits(s: str) -> int:
    # count occurrences of known words as whole tokens where possible
    tokens = HEBREW_WORD_RE.findall(s)
    if not tokens:
        return 0
    hits = 0
    for t in tokens:
        if t in HE_COMMON:
            hits += 1
    # also reward common bigrams (very cheap “language model”)
    joined = " ".join(tokens)
    for bg in ["ניהול מוצר", "מחקר שוק", "ניתוח מתחרים", "קהלי מטרה"]:
        if bg in joined:
            hits += 2
    return hits


def latin_integrity_score(orig: str, cand: str) -> int:
    """
    Reward candidates that keep obvious Latin abbreviations / runs intact.
    Penalize those that reverse them.
    """
    orig_runs = LATIN_RUN_RE.findall(orig)
    if not orig_runs:
        return 0

    score = 0
    for run in orig_runs:
        if run in cand:
            score += 2
        elif run[::-1] in cand:
            score -= 3
        else:
            # missing entirely: mild penalty
            score -= 1

    # extra reward for known abbreviations staying correct
    for abbr in LATIN_KEEP:
        if abbr in orig:
            score += 2 if abbr in cand else -2
    return score


def candidate_score(orig: str, cand: str) -> int:
    cand = cleanup_line(cand)
    if not cand:
        return -10**9

    score = 0

    # Prefer lines that contain more “real” Hebrew words we know
    score += 10 * hebrew_word_hits(cand)

    # If it contains Hebrew at all, slightly reward (vs garbage)
    if contains_hebrew(cand):
        score += 2

    # Avoid obvious reversal artifacts
    if looks_bad_leading_punct(cand):
        score -= 4

    # Preserve Latin segments
    score += latin_integrity_score(orig, cand)

    # Penalize lines that are almost pure punctuation/garbage
    if len(re.sub(r"[\W_]+", "", cand)) < 2:
        score -= 5

    return score


def best_rtl_fix(s: str) -> str:
    """
    Generate multiple variants and pick the best with scoring.
    Works even when some blocks in the same PDF are stored reversed.
    """
    s0 = cleanup_line(s)
    if not s0 or not contains_hebrew(s0):
        return s0

    candidates = []

    # 1) As-is
    candidates.append(s0)

    # 2) Hebrew tokens reversed only (often fixes "רצומ לוהינ" without killing TAM/SAM)
    candidates.append(reverse_hebrew_tokens_only(s0))

    # 3) Word order reversed (sometimes PDF flips word order but not letters)
    candidates.append(reverse_words_preserving_spaces(s0))

    # 4) Full reverse (hard fix for fully mirrored blocks)
    candidates.append(s0[::-1])

    if get_display is not None:
        # 5) bidi on as-is
        candidates.append(get_display(s0))

        # 6) bidi after reversing Hebrew tokens
        candidates.append(get_display(reverse_hebrew_tokens_only(s0)))

        # 7) bidi after full reverse
        candidates.append(get_display(s0[::-1]))

        # 8) bidi after reversing word order
        candidates.append(get_display(reverse_words_preserving_spaces(s0)))

    # Pick best by score
    best = max(candidates, key=lambda c: candidate_score(s0, c))
    return cleanup_line(best)


def postprocess_lines(lines: list[str]) -> list[str]:
    out = []
    i = 0
    while i < len(lines):
        s = cleanup_line(lines[i])
        if not s:
            i += 1
            continue

        # join hyphen linebreak for English (avoid breaking bullets)
        if s.endswith("-") and i + 1 < len(lines):
            nxt = cleanup_line(lines[i + 1])
            if nxt and re.match(r"^[A-Za-z]", nxt):
                s = s[:-1] + nxt
                i += 2
            else:
                i += 1
        else:
            i += 1

        out.append(best_rtl_fix(s))

    return out


def pick_title(lines: list[str]) -> str | None:
    for s in lines[:8]:
        s = cleanup_line(s)
        if len(s) >= 4 and not re.fullmatch(r"\d+", s):
            return s
    return None


def convert(pdf_path: Path, out_path: Path) -> None:
    doc = fitz.open(pdf_path)

    md = []
    md.append(f"# {pdf_path.stem}")
    md.append("")

    for idx, page in enumerate(doc, start=1):
        raw_lines = extract_page_lines(page)
        fixed = postprocess_lines(raw_lines)

        md.append(f"## Slide {idx}")
        title = pick_title(fixed)
        if title:
            md.append(f"**{title}**")
            md.append("")

        for line in fixed:
            if line.startswith(("• ", "- ", "– ", "— ")):
                md.append(f"- {line[2:].strip()}")
            else:
                md.append(line)
        md.append("")

    out_path.write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")
    doc.close()


def main():
    ap = argparse.ArgumentParser(description="Convert slide-like PDF to Markdown with robust Hebrew RTL fixes.")
    ap.add_argument("--pdf", help="Path to PDF file")
    ap.add_argument("--out", help="Output .md path (default: same name next to pdf)")
    args = ap.parse_args()

    pdf_in = args.pdf or input("PDF filename (in this folder or full path): ").strip().strip('"').strip("'")
    pdf_path = Path(pdf_in).expanduser().resolve()

    if not pdf_path.exists():
        print(f"ERROR: file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    if pdf_path.suffix.lower() != ".pdf":
        print("ERROR: input must be a .pdf", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out).expanduser().resolve() if args.out else pdf_path.with_suffix(".md")

    if get_display is None:
        print("WARN: python-bidi not installed; will still try non-bidi fixes. Install: pip install python-bidi", file=sys.stderr)

    convert(pdf_path, out_path)
    print(f"OK: wrote {out_path}")


if __name__ == "__main__":
    main()