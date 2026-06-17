![Analysis](https://github.com/avanit-singh/Customer-Churn-Analysis-for-Banking-Customers/actions/workflows/run_analysis.yml/badge.svg)

# Customer Churn Analysis — Banking Domain

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](YOUR_COLAB_LINK)

## Overview
End-to-end churn analysis for a banking customer dataset.
Identifies churn drivers, high-risk customer segments, and retention
opportunities using Python (Pandas), SQL, and Power BI.

---

## Project Structure
banking-customer-churn-analysis/
├── data/
│   └── banking_customers.csv    # 20 sample banking customers
├── notebooks/
│   └── churn_analysis.py        # Python analysis with outputs
├── sql/
│   └── churn_queries.sql        # SQL queries for churn KPIs
└── README.md

---

## Key Analyses Performed
1. Overall Churn Rate & Retention Rate
2. Churn segmentation by Age Group
3. Churn segmentation by Account Type
4. Churn segmentation by Credit Score Band
5. High-Risk Segment Identification
6. Retained vs Churned comparison (balance, credit, activity)

---

## Key Findings
| Metric | Value |
|---|---|
| Overall Churn Rate | 45% |
| Retention Rate | 55% |
| High-Risk Segment Churn Rate | 2x+ above average |
| Lowest Churn Age Group | 40–50 years |
| Highest Risk: Low credit + low transactions + new accounts |

---

## Key Metrics Analysed
Customer Retention Rate · Churn Rate · Credit Score Distribution ·
Account Activity · Product Utilization

---

## How to Run
```bash
pip install pandas
python notebooks/churn_analysis.py
```

---

## Author
**Avanit Singh** — Data Engineer | Fintech & BFSI Domain
[LinkedIn](https://linkedin.com/in/[your-id]) · [GitHub](https://github.com/avanit-singh)
