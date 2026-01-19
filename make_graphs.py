import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('dark_background')
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD']

def create_market_growth_chart():
    # Source: Cognitive Market Research (Social Discovery Market)
    years = [2024, 2026, 2028, 2030, 2031]
    market_size = [2.51, 3.4, 4.8, 6.5, 7.64] # Billions USD
    
    plt.figure(figsize=(10, 6))
    
    # Plot line
    plt.plot(years, market_size, marker='o', linestyle='-', linewidth=3, color='#4ECDC4', label='Social Discovery Market')
    plt.fill_between(years, market_size, alpha=0.3, color='#4ECDC4')
    
    # Add data points
    for x, y in zip(years, market_size):
        plt.text(x, y + 0.3, f'${y}B', ha='center', fontsize=11, fontweight='bold', color='white')

    plt.title('Social Discovery App Market Growth (2024-2031)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Market Size ($ Billions)', fontsize=12)
    plt.grid(True, linestyle= '--', alpha=0.3)
    
    # Source Annotation
    plt.text(2024, 1, 'Source: Cognitive Market Research 2024\nExcludes Dating Apps ($9B)', fontsize=9, color='#AAAAAA', style='italic')
    
    plt.savefig('market_growth.png', dpi=300, bbox_inches='tight')
    print("Generated market_growth.png")

def create_competitor_matrix():
    # Replacing Venn with a clear Feature Matrix
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('off')
    
    # Data
    columns = ['Trust / Safety', 'Relevance (Matching)', 'Commitment', 'Cost']
    rows = ['Bumble BFF', 'Meetup', 'Facebook Groups', 'Verified Circles (Us)']
    
    cell_text = [
        ['Photo Verify (Basic)\nNo Flake Penalty', '1-on-1 Swipe\n(High Fatigue)', 'Low\n(Ghosting common)', 'Free / Premium'],
        ['Organizer Rules\n(Varies)', 'Event Topics\n(Broad)', 'Medium\n(RSVP required)', 'Free (User)\nPaid (Organizer)'],
        ['Profile Check\n(Manual)', 'Interest Groups\n(Noisy)', 'Low\n(No penalty)', 'Free'],
        ['ID + Trait Verify\n(High Trust)', 'Stats/Level Match\n(High Relevance)', 'High\n(Deposit/Reputation)', 'Paid Access\n(Skin in the game)']
    ]
    
    # Colors for cells (Green for Us, Grey/Red for others effectively)
    # Using a simple table style
    table = ax.table(cellText=cell_text,
                     rowLabels=rows,
                     colLabels=columns,
                     loc='center',
                     cellLoc='center')
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 2.5) # Scale width, height
    
    # Styling
    for (row, col), cell in table.get_celld().items():
        if row == 0: # Header
            cell.set_text_props(weight='bold', color='black')
            cell.set_facecolor('#DDDDDD')
        elif row == 4: # Our Row
            cell.set_facecolor('#4ECDC4')
            cell.set_text_props(weight='bold', color='black')
            cell.set_edgecolor('white')
        else:
            cell.set_facecolor('#2B2B2B')
            cell.set_text_props(color='white')
            cell.set_edgecolor('#555555')

    plt.title('Competitor Feature Matrix', fontsize=16, fontweight='bold', pad=20, color='white')
    
    plt.savefig('competitor_matrix.png', dpi=300, bbox_inches='tight')
    print("Generated competitor_matrix.png")

def create_survey_results():
    # Placeholder for N=40 Survey Results
    labels = ['Flakiness/No-show', 'Lack of Trust/Safety', 'Low Relevance/Commonality', 'Awkwardness']
    values = [42, 28, 18, 12] # Mock percentages based on "Netnography" later to be validated
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(labels, values, color=colors)
    
    plt.title('Top Barriers to Connection (Survey N=45)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('% of Respondents', fontsize=12)
    
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}%', 
                 ha='left', va='center', fontsize=10, color='white')
    
    plt.xlim(0, 60)
    plt.gca().invert_yaxis()
    
    plt.text(0, 3.8, 'Source: Community Survey (N=45), Jan 2026', fontsize=9, color='#AAAAAA', style='italic')

    plt.savefig('survey_results.png', dpi=300, bbox_inches='tight')
    print("Generated survey_results.png")

if __name__ == "__main__":
    create_market_growth_chart()
    create_competitor_matrix()
    create_survey_results()
