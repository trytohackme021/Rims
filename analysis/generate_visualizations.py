import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set custom editorial styling
plt.style.use('seaborn-v0_8-ticks' if 'seaborn-v0_8-ticks' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 11

df = pd.read_csv(r"C:\Users\Asus\.gemini\antigravity\scratch\rims_library_consulting_taskforce\data\rims_collection_audit_2026.csv")
out_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\rims_library_consulting_taskforce\analysis"

# -------------------------------------------------------------
# GRAPH 1: Departmental Utilization Profile (Physical vs Digital)
# -------------------------------------------------------------
dept_data = df.groupby('department')[['times_issued_last_year', 'downloads_last_year']].sum().reset_index()
dept_data['total'] = dept_data['times_issued_last_year'] + dept_data['downloads_last_year']
dept_data = dept_data.sort_values(by='total', ascending=True)

fig, ax = plt.subplots(figsize=(10, 5.5))
y_pos = np.arange(len(dept_data))
h = 0.38

# Emerald and Terracotta palette
rects1 = ax.barh(y_pos - h/2, dept_data['times_issued_last_year'], h, label='Physical Checkouts', color='#064e3b', edgecolor='#022c22')
rects2 = ax.barh(y_pos + h/2, dept_data['downloads_last_year'], h, label='Electronic Downloads', color='#c2410c', edgecolor='#7c2d12')

ax.set_yticks(y_pos)
ax.set_yticklabels(dept_data['department'], fontsize=10, fontweight='bold')
ax.set_xlabel('Annual Academic Interactions (Consultations & Retrievals)', fontsize=11, fontweight='bold')
ax.set_title('Figure 1: Comparative Academic School Utilization Breakdown', pad=14, loc='left', color='#0f172a')
ax.legend(frameon=True, loc='lower right', facecolor='#f8fafc', edgecolor='#cbd5e1')

# Add direct value labels
for r in rects1:
    w = r.get_width()
    ax.text(w + 15, r.get_y() + r.get_height()/2, f'{int(w)}', va='center', ha='left', fontsize=8.5, fontweight='bold', color='#064e3b')
for r in rects2:
    w = r.get_width()
    ax.text(w + 15, r.get_y() + r.get_height()/2, f'{int(w)}', va='center', ha='left', fontsize=8.5, fontweight='bold', color='#c2410c')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{out_dir}/figure_1_department_utilization.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 2: Imprint Currency vs. Circulation Velocity (Books)
# -------------------------------------------------------------
books = df[df['resource_type'] == 'book'].copy()

fig, ax = plt.subplots(figsize=(10, 5.5))
scatter = ax.scatter(
    books['publication_year'], 
    books['times_issued_last_year'], 
    c=books['satisfaction_score'], 
    cmap='YlGn', 
    s=70, 
    edgecolors='#1e293b', 
    alpha=0.85, 
    linewidth=0.8
)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Student Satisfaction Rating (1-5)', rotation=270, labelpad=16, fontweight='bold')

# Trend curve
sns.regplot(data=books, x='publication_year', y='times_issued_last_year', scatter=False, ax=ax, color='#b91c1c', line_kws={'linewidth': 2.5, 'linestyle': '-'})

ax.axvline(x=2015, color='#475569', linestyle=':', linewidth=1.8)
ax.text(2003, 50, "Stagnant Pre-2015 Tier\n(Avg. <1.4 Checkouts)", bbox=dict(boxstyle='round,pad=0.5', facecolor='#fee2e2', edgecolor='#b91c1c', alpha=0.9), fontsize=9, fontweight='bold')
ax.text(2016, 56, "Active Syllabus Titles\n(Up to 64 Checkouts)", bbox=dict(boxstyle='round,pad=0.5', facecolor='#dcfce7', edgecolor='#15803d', alpha=0.9), fontsize=9, fontweight='bold')

ax.set_title('Figure 2: Monograph Circulation Velocity Relative to Publication Vintage', pad=14, loc='left', color='#0f172a')
ax.set_xlabel('Imprint / Edition Vintage Year', fontweight='bold')
ax.set_ylabel('Annual Circulatory Checkouts (Times Issued)', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{out_dir}/figure_2_issues_vs_publication_year.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 3: Strategic Portfolio Quadrant (Cost vs. Utilization)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))
df['total_use'] = df['times_issued_last_year'] + df['downloads_last_year']

color_dict = {'book': '#0284c7', 'journal': '#dc2626', 'e-resource': '#16a34a'}
for r_type, c in color_dict.items():
    sub = df[df['resource_type'] == r_type]
    ax.scatter(sub['total_use'], sub['annual_cost'], label=f"{r_type.title()} Holdings", color=c, alpha=0.75, s=65, edgecolors='black', linewidth=0.5)

ax.axhline(y=25000, color='#94a3b8', linestyle='--', linewidth=1)
ax.axvline(x=12, color='#94a3b8', linestyle='--', linewidth=1)

# Four Strategic Quadrants
ax.text(2, 80000, "QUADRANT I: CRITICAL REVISION\n(Niche Serials: High Cost / Low Downloads)", bbox=dict(boxstyle='square,pad=0.5', facecolor='#fef2f2', edgecolor='#ef4444'), fontsize=8.5, fontweight='bold', color='#991b1b')
ax.text(65, 8000, "QUADRANT II: HIGH-RETURN COMMONS\n(Course Texts: High Circulation / Modest Cost)", bbox=dict(boxstyle='square,pad=0.5', facecolor='#f0fdf4', edgecolor='#22c55e'), fontsize=8.5, fontweight='bold', color='#166534')
ax.text(70, 38000, "QUADRANT III: DIGITAL EXPANSION\n(E-Resource Bundles: High Access Volume)", bbox=dict(boxstyle='square,pad=0.5', facecolor='#eff6ff', edgecolor='#3b82f6'), fontsize=8.5, fontweight='bold', color='#1e40af')

ax.set_title('Figure 3: Portfolio Efficiency Matrix (Annual Cost vs. Total Usage Yield)', pad=14, loc='left', color='#0f172a')
ax.set_xlabel('Combined Total Usages (Physical Issues + Digital Downloads)', fontweight='bold')
ax.set_ylabel('Annual Procurement / Subscription Expense (INR ₹)', fontweight='bold')
ax.legend(loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{out_dir}/figure_3_cost_vs_usage.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 4: Temporal Footfall Dynamic Across Operating Slots
# -------------------------------------------------------------
slot_summary = df['visit_time_slot'].value_counts().reindex([
    "Slot A: 09:00 - 11:30", 
    "Slot B: 11:30 - 13:30", 
    "Slot C: 13:30 - 15:30", 
    "Slot D: 15:30 - 17:00"
])

fig, ax = plt.subplots(figsize=(9, 5))
x_labels = ["09:00 - 11:30\n(Morning Session)", "11:30 - 13:30\n(Midday Peak)", "13:30 - 15:30\n(Afternoon Lull)", "15:30 - 17:00\n(Pre-Close Choke)"]
palette_slots = ['#1d4ed8', '#047857', '#d97706', '#b91c1c']

bars = ax.bar(x_labels, slot_summary.values, color=palette_slots, width=0.52, edgecolor='#0f172a', linewidth=1)

for b in bars:
    val = b.get_height()
    pct = (val / len(df)) * 100
    ax.text(b.get_x() + b.get_width()/2, val + 2.5, f"{int(val)} ({pct:.1f}%)", ha='center', va='bottom', fontsize=9.5, fontweight='bold')

ax.set_ylim(0, 140)
ax.set_title('Figure 4: Operating Hours Inundation & Late Afternoon Chokepoint', pad=14, loc='left', color='#0f172a')
ax.set_ylabel('Sample Consultation Frequency', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{out_dir}/figure_4_visits_by_time_slot.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 5: Seniority-Linked Sentiment Erosion
# -------------------------------------------------------------
cohort_order = [
    "Year 1 (Freshman UG)", 
    "Year 2 (Sophomore UG)", 
    "Year 3 (Final Year UG)", 
    "Master Level (PG-1)", 
    "Master Level (PG-2)"
]

fig, ax = plt.subplots(figsize=(10, 5.5))
palette_sen = ['#bbf7d0', '#86efac', '#fde047', '#fdba74', '#fca5a5']
sns.boxplot(data=df, x='student_year', y='satisfaction_score', order=cohort_order, palette=palette_sen, ax=ax, width=0.48, fliersize=3)

# Calculate and plot means
cohort_means = df.groupby('student_year')['satisfaction_score'].mean().reindex(cohort_order)
for idx, c_name in enumerate(cohort_order):
    m_val = cohort_means[c_name]
    ax.scatter(idx, m_val, color='#991b1b', s=50, zorder=5)
    ax.text(idx, m_val + 0.18, f"Avg: {m_val:.2f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#991b1b')

ax.set_ylim(0.5, 5.5)
ax.set_title('Figure 5: Student Satisfaction Index Across Academic Seniority Tiers', pad=14, loc='left', color='#0f172a')
ax.set_xlabel('Academic Cohort Classification', fontweight='bold')
ax.set_ylabel('Satisfaction Likert Score (1: Poor, 5: Excellent)', fontweight='bold')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f"{out_dir}/figure_5_satisfaction_by_year.png", dpi=300)
plt.close()

print("All 5 unique charts successfully generated!")
