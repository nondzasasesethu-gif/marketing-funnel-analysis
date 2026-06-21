import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank-additional-full.csv', sep=';')

# ── Funnel Data ────────────────────────────────────────────
funnel_stages = ['Contacted', 'Engaged', 'Warm Leads', 'Converted']
funnel_counts = [41188, 33553, 1515, 4640]

# ── Plot 1: Funnel Chart ───────────────────────────────────
plt.figure(figsize=(8, 5))
colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']
bars = plt.barh(funnel_stages, funnel_counts, color=colors)
plt.xlabel('Number of People')
plt.title('Marketing Funnel - Stage Performance')
for bar, count in zip(bars, funnel_counts):
    plt.text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2,
             f'{count:,}', va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('funnel_chart.png', dpi=150)
plt.show()

# ── Plot 2: Conversion by Contact Method ──────────────────
plt.figure(figsize=(8, 5))
contact_conv = df.groupby('contact')['y'].apply(lambda x: (x == 'yes').mean() * 100)
contact_conv.plot(kind='bar', color=['#2196F3', '#4CAF50'], edgecolor='black')
plt.title('Conversion Rate by Contact Method')
plt.ylabel('Conversion Rate (%)')
plt.xlabel('Contact Method')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('contact_conversion.png', dpi=150)
plt.show()

# ── Plot 3: Conversion by Month ───────────────────────────
plt.figure(figsize=(10, 5))
month_order = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
month_conv = df.groupby('month')['y'].apply(lambda x: (x == 'yes').mean() * 100)
month_conv = month_conv.reindex(month_order).dropna()
month_conv.plot(kind='bar', color='#9C27B0', edgecolor='black')
plt.title('Conversion Rate by Month')
plt.ylabel('Conversion Rate (%)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_conversion.png', dpi=150)
plt.show()

print("All charts saved!")

# ── Key Metrics Summary ────────────────────────────────────
print("\n===== FUNNEL ANALYSIS SUMMARY =====")
print(f"Total Contacted:     41,188")
print(f"Overall Conversion:  11.3%")
print(f"Best Contact Method: Cellular (14.7%)")
print(f"Best Month:          March (50%)")
print(f"Worst Month:         May (6.4%)")
print(f"Drop-off Alert:      96.3% of leads were cold (never previously contacted)")
print("====================================")