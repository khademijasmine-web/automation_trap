# Targeting the High-Value Risk Zone
### Prioritising AI-Reskilling Investment in the Age of AI

**MAN6777 — Data Analytics Portfolio (Assessment 3)**
Author: Yasaman Khademi Gilchalan

---

## Project Overview

This project helps a **Chief People Officer (CPO)** decide which employee groups to prioritise for AI-reskilling investment, given a limited learning & development budget.

Using 5,000 global job listings (2010–2025), it identifies the **High-Value Risk Zone** — roles that combine high salary with high automation risk — and shows that AI engagement is the strongest lever for reducing displacement risk while also raising pay.

## Key Findings

- **22.4%** of all roles fall into the High-Value Risk Zone (high pay + high automation risk).
- A linear regression shows AI intensity explains **77%** of the variation in automation risk (R² = 0.77, slope = −0.75, p < 0.05).
- A correlation matrix shows AI engagement is linked to lower risk (r = −0.88), higher pay (r = 0.42), and faster salary growth (r = 0.67).
- AI-engaged roles earn a **58% salary premium** ($83,846 vs $53,124).
- Most-exposed industries: **Government (25.8%), Healthcare (23.9%), Education (23.7%)**.

## Recommendations

1. Launch a targeted AI-reskilling programme for the High-Value Risk Zone.
2. Start with the most-exposed industries (Government, Healthcare, Education); Finance can wait.

## Repository Structure

```
├── README.md                          <- This file
├── data/
│   └── ai_impact_jobs_2010_2025.xlsx  <- Raw dataset (5,000 rows, 22 columns)
└── notebooks/
    └── automation_analysis.ipynb      <- Clean, commented, reproducible analysis
```

## How to Run

1. Clone this repository.
2. Install dependencies:
   ```
   pip install pandas numpy matplotlib scipy statsmodels openpyxl
   ```
3. Open `notebooks/automation_analysis.ipynb` and select **Run All**.
   The notebook reads the dataset from `../data/` and regenerates every figure and statistic with no manual steps.

## Methods

| Technique | Tool | Purpose |
|-----------|------|---------|
| Quadrant segmentation (median split) | Python / Power BI | Group roles for budget allocation |
| Linear regression | Excel ToolPak / Python | Measure the AI–risk relationship |
| Correlation matrix | Python (pandas) | Map links among AI, risk, salary, salary growth |
| Dashboard visualisation | Power BI | Communicate findings |

## Data Source

Global AI Impact on Jobs (2010–2025), a synthetic dataset grounded in real labour-market trends. Licensed under ODC Public Domain Dedication and Licence (PDDL).

> *Note: the dataset is synthetic and intended for research and education. Figures should be validated against an organisation's own HR data before committing budget.*
