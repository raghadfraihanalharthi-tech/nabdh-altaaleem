"""
Nabdh Al-Taaleem — Women in Saudi ICT
Case Study Analysis Script
Author: Raghad Al-Blahdi
Data Source: open.data.gov.sa
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

# ── Setup ──────────────────────────────────────────────
output_dir = os.path.join(os.path.dirname(__file__), '..', 'report', 'charts')
os.makedirs(output_dir, exist_ok=True)

plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

DARK  = '#07111f'
DARK2 = '#0c1d33'
GREEN = '#10b981'
CYAN  = '#06b6d4'
AMBER = '#f59e0b'
RED   = '#ef4444'
MUTED = '#7ca3c8'
WHITE = '#e2e8f0'

# ── Load Data ──────────────────────────────────────────
data_dir = os.path.join(os.path.dirname(__file__), '..', 'dataset')

df_ict = pd.read_csv(
    os.path.join(data_dir, 'women_participation_ICT.csv'),
    encoding='utf-8-sig'
)
df_ratio = pd.read_csv(
    os.path.join(data_dir, 'male_female_ratio_2024.csv'),
    encoding='utf-8-sig'
)

# Clean participation data
df_ict = df_ict[['السنة', 'القيمة']].dropna()
df_ict.columns = ['year', 'value']
df_ict['value'] = df_ict['value'].astype(str).str.replace('%', '').astype(float)
df_ict['year'] = df_ict['year'].astype(int)

# Clean ratio data
df_ratio = df_ratio.dropna()
df_ratio.columns = ['year', 'female', 'male']
df_ratio = df_ratio[df_ratio['year'] != '']
female_pct = float(str(df_ratio['female'].iloc[0]).replace('%','')) * 100 if float(str(df_ratio['female'].iloc[0]).replace('%','')) <= 1 else float(str(df_ratio['female'].iloc[0]).replace('%',''))
male_pct = 100 - female_pct

print("=" * 50)
print("NABDH AL-TAALEEM — DATA ANALYSIS")
print("=" * 50)
print(f"\nWomen's ICT Participation Data:")
print(df_ict.to_string(index=False))
print(f"\nGender Ratio 2024: Female {female_pct}% / Male {male_pct}%")

# ── Key Statistics ─────────────────────────────────────
start_val = df_ict['value'].iloc[0]
end_val   = df_ict['value'].iloc[-1]
growth    = end_val - start_val
avg_growth = growth / (len(df_ict) - 1)

print(f"\nKey Findings:")
print(f"  Start (2020):      {start_val:.2f}%")
print(f"  End   (2024):      {end_val:.2f}%")
print(f"  Total Growth:      +{growth:.2f}%")
print(f"  Avg Annual Growth: +{avg_growth:.2f}%")
print(f"  vs Vision 2030:    30% target — {'ACHIEVED' if end_val >= 30 else 'NOT YET'}")
print(f"  vs Global ITU:     <33% — Saudi at {end_val:.1f}% ({'Above' if end_val >= 33 else 'Below'} benchmark)")

# ── Chart 1: Participation Trend ───────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5))
fig.patch.set_facecolor(DARK)
ax.set_facecolor(DARK2)

ax.fill_between(df_ict['year'], df_ict['value'], alpha=0.12, color=GREEN)
ax.plot(df_ict['year'], df_ict['value'], color=GREEN, linewidth=2.5, zorder=5)
ax.scatter(df_ict['year'], df_ict['value'], color=GREEN, s=70, zorder=6)

for _, row in df_ict.iterrows():
    ax.annotate(f"{row['value']:.2f}%",
                xy=(row['year'], row['value']),
                xytext=(0, 12), textcoords='offset points',
                ha='center', fontsize=9.5, color=WHITE, fontweight='bold')

ax.axhline(30, color=AMBER, linestyle='--', linewidth=1.2, alpha=0.7)
ax.axhline(33, color=CYAN,  linestyle='--', linewidth=1.2, alpha=0.6)

ax.text(df_ict['year'].max() + 0.05, 30.5, 'Vision 2030 Target (30%)', color=AMBER, fontsize=8.5, va='bottom')
ax.text(df_ict['year'].max() + 0.05, 33.5, 'Global ITU Benchmark (<33%)', color=CYAN, fontsize=8.5, va='bottom')

ax.set_xlim(2019.7, 2025.2)
ax.set_ylim(0, 45)
ax.set_xticks(df_ict['year'])
ax.set_xlabel('Year', color=MUTED, fontsize=10)
ax.set_ylabel('Participation Rate (%)', color=MUTED, fontsize=10)
ax.tick_params(colors=MUTED)
for spine in ax.spines.values():
    spine.set_edgecolor('#1e3a5a')

ax.set_title("Women's Participation Rate in Saudi ICT Sector (2020–2024)",
             color=WHITE, fontsize=13, fontweight='bold', pad=16)
ax.text(0.5, -0.13, 'Source: open.data.gov.sa | Benchmarks: ITU 2024, Vision 2030',
        transform=ax.transAxes, ha='center', fontsize=8, color=MUTED)

plt.tight_layout()
chart1_path = os.path.join(output_dir, 'chart1_participation_trend.png')
plt.savefig(chart1_path, facecolor=DARK, bbox_inches='tight')
plt.close()
print(f"\n  Chart 1 saved: {chart1_path}")

# ── Chart 2: Gender Ratio Donut ────────────────────────
fig, ax = plt.subplots(figsize=(7, 6))
fig.patch.set_facecolor(DARK)
ax.set_facecolor(DARK)

sizes  = [male_pct, female_pct]
colors = ['#3d5a77', GREEN]
labels = [f'Male\n{male_pct:.0f}%', f'Female\n{female_pct:.0f}%']
explode = (0, 0.04)

wedges, texts = ax.pie(sizes, colors=colors, explode=explode,
                        startangle=90, wedgeprops=dict(width=0.55, edgecolor=DARK, linewidth=3))

ax.text(0, 0, f'{female_pct:.0f}%\nFemale', ha='center', va='center',
        fontsize=18, fontweight='bold', color=GREEN)

patches = [mpatches.Patch(color=c, label=l) for c, l in zip(colors, labels)]
ax.legend(handles=patches, loc='lower center', bbox_to_anchor=(0.5, -0.08),
          ncol=2, frameon=False,
          labelcolor=WHITE, fontsize=10)

ax.set_title('ICT Workforce Gender Distribution — Saudi Arabia 2024',
             color=WHITE, fontsize=12, fontweight='bold', pad=14)
ax.text(0.5, -0.15, 'Source: open.data.gov.sa',
        transform=ax.transAxes, ha='center', fontsize=8, color=MUTED)

plt.tight_layout()
chart2_path = os.path.join(output_dir, 'chart2_gender_ratio.png')
plt.savefig(chart2_path, facecolor=DARK, bbox_inches='tight')
plt.close()
print(f"  Chart 2 saved: {chart2_path}")

# ── Chart 3: Comparison Bar Chart ─────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5))
fig.patch.set_facecolor(DARK)
ax.set_facecolor(DARK2)

categories = ['Saudi Arabia\n2020', 'Saudi Arabia\n2024', 'Vision 2030\nTarget', 'Global ITU\nBenchmark']
values     = [24.08, 34.50, 30.00, 33.00]
bar_colors = [MUTED, GREEN, AMBER, CYAN]

bars = ax.bar(categories, values, color=bar_colors, width=0.5,
              edgecolor=DARK, linewidth=1.5)

for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.6,
            f'{val:.1f}%', ha='center', va='bottom',
            fontsize=11, fontweight='bold', color=WHITE)

ax.set_ylim(0, 45)
ax.set_ylabel('Participation Rate (%)', color=MUTED, fontsize=10)
ax.tick_params(colors=MUTED)
ax.set_title("Saudi Arabia's ICT Gender Participation vs Benchmarks",
             color=WHITE, fontsize=13, fontweight='bold', pad=16)
ax.text(0.5, -0.16, 'Sources: open.data.gov.sa | Vision 2030 | ITU 2024',
        transform=ax.transAxes, ha='center', fontsize=8, color=MUTED)

for spine in ax.spines.values():
    spine.set_edgecolor('#1e3a5a')
ax.tick_params(axis='x', colors=WHITE, labelsize=9.5)

plt.tight_layout()
chart3_path = os.path.join(output_dir, 'chart3_comparison.png')
plt.savefig(chart3_path, facecolor=DARK, bbox_inches='tight')
plt.close()
print(f"  Chart 3 saved: {chart3_path}")

print("\n  All charts generated successfully.")
print("  Run generate_report.py next to create the PDF report.")
