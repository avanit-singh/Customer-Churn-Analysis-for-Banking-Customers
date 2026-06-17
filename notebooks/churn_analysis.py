# ================================================================
# Customer Churn Analysis — Banking Domain
# Author  : Avanit Singh
# Stack   : Python (Pandas) | SQL | Power BI
# Purpose : Identify churn drivers and high-risk customer segments
# ================================================================

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# ── 1. Load Data ─────────────────────────────────────────────
df = pd.read_csv('data/banking_customers.csv')
print(f"✅ Data loaded: {len(df)} customers")
print(f"\n📋 Dataset Info:")
print(df.dtypes)
print(f"\n📊 First 5 rows:")
print(df.head())

# ── 2. Data Cleaning ─────────────────────────────────────────
print(f"\n🔍 Null values check:")
print(df.isnull().sum())
df = df.dropna()
print(f"✅ Clean records: {len(df)}")

# ── 3. Overall Churn Rate ────────────────────────────────────
total        = len(df)
churned      = df['churned'].sum()
retained     = total - churned
churn_rate   = (churned / total) * 100

print(f"\n{'='*50}")
print(f"📊 CHURN SUMMARY")
print(f"{'='*50}")
print(f"Total Customers   : {total}")
print(f"Churned           : {churned}  ({churn_rate:.1f}%)")
print(f"Retained          : {retained}  ({100-churn_rate:.1f}%)")

# ── 4. Churn by Age Group ────────────────────────────────────
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 30, 40, 50, 100],
    labels=['Under 30', '30-40', '40-50', 'Above 50']
)
age_churn = df.groupby('age_group', observed=True)['churned'].agg(
    Total='count',
    Churned='sum'
)
age_churn['Churn Rate %'] = (age_churn['Churned'] / age_churn['Total'] * 100).round(1)
print(f"\n📊 CHURN BY AGE GROUP:")
print(age_churn.to_string())

# ── 5. Churn by Account Type ─────────────────────────────────
acct_churn = df.groupby('account_type')['churned'].agg(
    Total='count', Churned='sum'
)
acct_churn['Churn Rate %'] = (acct_churn['Churned'] / acct_churn['Total'] * 100).round(1)
print(f"\n📊 CHURN BY ACCOUNT TYPE:")
print(acct_churn.to_string())

# ── 6. Churn by Credit Score Band ───────────────────────────
df['credit_band'] = pd.cut(
    df['credit_score'],
    bins=[0, 550, 650, 720, 900],
    labels=['Poor <550', 'Fair 550-650', 'Good 650-720', 'Excellent 720+']
)
credit_churn = df.groupby('credit_band', observed=True)['churned'].agg(
    Total='count', Churned='sum'
)
credit_churn['Churn Rate %'] = (
    credit_churn['Churned'] / credit_churn['Total'] * 100
).round(1)
print(f"\n📊 CHURN BY CREDIT SCORE BAND:")
print(credit_churn.to_string())

# ── 7. High-Risk Segment Identification ─────────────────────
high_risk = df[
    (df['credit_score'] < 600) &
    (df['num_transactions_6m'] < 5) &
    (df['months_active'] < 12)
]
overall_rate   = df['churned'].mean()
highrisk_rate  = high_risk['churned'].mean() if len(high_risk) > 0 else 0
multiplier     = highrisk_rate / overall_rate if overall_rate > 0 else 0

print(f"\n{'='*50}")
print(f"🚨 HIGH-RISK SEGMENT ANALYSIS")
print(f"{'='*50}")
print(f"Criteria  : Credit < 600 | Txns < 5 | Active < 12 months")
print(f"Customers : {len(high_risk)}")
print(f"Churn Rate in Segment : {highrisk_rate*100:.1f}%")
print(f"Overall Churn Rate    : {overall_rate*100:.1f}%")
print(f"Risk Multiplier       : {multiplier:.1f}x higher than average")

# ── 8. Key Metrics Summary ───────────────────────────────────
retained_df = df[df['churned'] == 0]
churned_df  = df[df['churned'] == 1]

print(f"\n{'='*50}")
print(f"📈 KEY METRICS COMPARISON")
print(f"{'='*50}")
print(f"{'Metric':<30} {'Retained':>12} {'Churned':>12}")
print(f"{'-'*54}")
print(f"{'Avg Balance (INR)':<30} {retained_df['balance'].mean():>12,.0f} {churned_df['balance'].mean():>12,.0f}")
print(f"{'Avg Credit Score':<30} {retained_df['credit_score'].mean():>12.0f} {churned_df['credit_score'].mean():>12.0f}")
print(f"{'Avg Transactions (6m)':<30} {retained_df['num_transactions_6m'].mean():>12.1f} {churned_df['num_transactions_6m'].mean():>12.1f}")
print(f"{'Avg Months Active':<30} {retained_df['months_active'].mean():>12.1f} {churned_df['months_active'].mean():>12.1f}")

print(f"\n✅ Churn Analysis completed successfully.")
print(f"🔑 Key Finding: High-risk segment churns at {multiplier:.1f}x the average rate.")
print(f"📌 Recommendation: Target customers with credit<600, low transactions, new accounts for retention campaigns.")
