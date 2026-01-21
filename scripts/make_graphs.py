from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Set style to white background (Clean Publication Style)
plt.style.use('default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True 
plt.rcParams['grid.alpha'] = 0.3

# Brand Colors (Clean)
col_primary = '#2A9D8F'   # Teal
col_secondary = '#E9C46A' # Gold
col_accent = '#E76F51'    # Coral
col_text = '#264653'      # Dark Blue

ASSETS_DIR = Path('presentation/assets')
ARCHIVE_DIR = Path('archive/old_assets')

def create_market_growth_chart():
    years = [2024, 2026, 2028, 2030, 2031]
    market_size = [2.51, 3.4, 4.8, 6.5, 7.64] # Billions USD
    
    plt.figure(figsize=(10, 6))
    
    # Plot line
    plt.plot(years, market_size, marker='o', linestyle='-', linewidth=3, color=col_primary, label='Social Discovery Market')
    plt.fill_between(years, market_size, alpha=0.1, color=col_primary)
    
    # Add data points
    for x, y in zip(years, market_size):
        plt.text(x, y + 0.3, f'${y}B', ha='center', fontsize=11, fontweight='bold', color=col_text)

    plt.title('Social Discovery App Market Growth (2024-2031)', fontsize=16, fontweight='bold', pad=20, color=col_text)
    plt.xlabel('Year', fontsize=12, color=col_text)
    plt.ylabel('Market Size ($ Billions)', fontsize=12, color=col_text)
    
    # Source Annotation
    plt.text(2024, 1, 'Source: Cognitive Market Research 2024\nExcludes Dating Apps ($9B)', fontsize=9, color='#555555', style='italic')
    
    out_path = ARCHIVE_DIR / 'social_discovery_market_growth.png'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f"Generated {out_path}")

def create_competitor_matrix():
    # Feature Matrix on White Background
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.axis('off')
    
    columns = ['Trust / Safety', '“Don’t go alone”\nstructure', 'Relevance', 'Cost model']
    rows = ['Bumble For Friends', 'Meetup', 'Timeleft', 'Verified Circles (Us)']
    
    cell_text = [
        ['Photo verification\n(optional)', 'None\n(user coordinates)', 'Profile + swiping', 'Freemium'],
        ['Organizer rules vary', 'Partial\n(events exist)', 'Topics/activities\n(broad)', 'Free (user)\nOrganizer pays'],
        ['Curated groups\n(public venues)', 'Yes\n(group dinner)', 'Limited\n(personalization)', 'Ticket / subscription'],
        ['Light verification\n+ rules + reporting', 'Yes\n(buddy/micro-group)', 'Circles by context\n(repeatable)', 'Paid events\n→ membership']
    ]
    
    # Create Table
    table = ax.table(cellText=cell_text,
                     rowLabels=rows,
                     colLabels=columns,
                     loc='center',
                     cellLoc='center')
    
    table.auto_set_font_size(False)
    table.set_fontsize(10) # Slightly smaller font to fit
    table.scale(1.2, 3.0) # Scale width, height
    
    # Detailed Styling
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#DDDDDD')
        if row == 0: # Header
            cell.set_text_props(weight='bold', color=col_text)
            cell.set_facecolor('#F0F0F0')
        elif row == 4: # Our Row (Index 4 because header is 0)
            cell.set_facecolor('#E0F2F1') # Very Light Teal
            cell.set_text_props(weight='bold', color='#004D40')
            cell.set_edgecolor(col_primary)
            cell.set_linewidth(2)
        else:
            cell.set_facecolor('white')
            cell.set_text_props(color=col_text)
    
    plt.title('Competitor Feature Matrix (B2C)', fontsize=16, fontweight='bold', pad=20, color=col_text)

    out_path = ASSETS_DIR / 'competitor_matrix.png'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f"Generated {out_path}")

def _load_survey_no_partner_counts(csv_path: Path) -> tuple[int, Counter[str]]:
    with csv_path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    # Columns are duplicated in the export; pick first non-empty answer.
    no_partner_a = header.index(
        'כשאתה רוצה לעשות פעילות (כמו ריצה או טניס) ואין לך פרטנר, מה אתה עושה בדרך כלל?'
    )
    no_partner_b = header.index(
        'כשאתה רוצה לעשות פעילות (כמו ריצה או טניס) ואין לך פרטנר, מה אתה עושה בדרך כלל?'
    ) + (14 - 6)  # second block offset

    counts: Counter[str] = Counter()
    n = 0
    for row in rows:
        if not any((c or '').strip() for c in row):
            continue
        n += 1
        answer = (row[no_partner_a] or '').strip() or (row[no_partner_b] or '').strip()
        if answer:
            counts[answer] += 1

    return n, counts


def create_survey_no_partner_chart():
    csv_path = Path('research/surveys/survey_responses_raw.csv')
    n, counts = _load_survey_no_partner_counts(csv_path)

    # Normalize/translate labels (keep deterministic order)
    order = [
        ('הולך לבד', 'Go alone'),
        ('מוותר', 'Give up'),
        ('לא עושה פעילויות כאלו', "Don’t do these activities"),
        ('מחפש בקבוצות ווטסאפ/פייסבוק', 'Search in WhatsApp/FB groups'),
        ('אחר', 'Other'),
    ]

    labels = []
    values = []
    for he, en in order:
        if he in counts:
            labels.append(en)
            values.append(round(counts[he] * 100 / n))

    plt.figure(figsize=(10, 6))
    bars = plt.barh(labels, values, color=[col_primary, col_accent, col_secondary, '#6C757D', '#AAAAAA'])

    plt.title(f'When there is no partner (Survey N={n})', fontsize=16, fontweight='bold', pad=20, color=col_text)
    plt.xlabel('% of respondents', fontsize=12, color=col_text)

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + 1,
            bar.get_y() + bar.get_height() / 2,
            f'{width}%',
            ha='left',
            va='center',
            fontsize=11,
            fontweight='bold',
            color=col_text,
        )

    plt.xlim(0, max(values) + 10)
    plt.gca().invert_yaxis()
    plt.text(0, len(labels) + 0.4, 'Source: research/surveys/survey_responses_raw.csv', fontsize=9, color='#555555', style='italic')

    out_path = ASSETS_DIR / 'survey_no_partner_behavior.png'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f"Generated {out_path}")

if __name__ == "__main__":
    create_competitor_matrix()
    create_survey_no_partner_chart()
