import pandas
import matplotlib.pyplot as plt

df = pd.read_excel('ai_impact_jobs_2010_2025.xlsx')
cols = ['ai_intensity_score', 'automation_risk_score',
        'salary_usd', 'salary_change_vs_prev_year_percent']
corr = df[cols].corr()
print(corr)
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1)

labels = ['AI Intensity', 'Automation Risk', 'Salary', 'Salary Growth %']
ax.set_xticks(range(4))
ax.set_yticks(range(4))
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_yticklabels(labels)

for i in range(4):
    for j in range(4):
        ax.text(j, i, f'{corr.iloc[i, j]:.2f}',
                ha='center', va='center')

plt.colorbar(im, label='Correlation (r)')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
