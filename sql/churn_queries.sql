-- ============================================================
-- Customer Churn Analysis — SQL Queries
-- Author: Avanit Singh
-- ============================================================

-- 1. Overall Churn Rate
SELECT
    COUNT(*)                                                      AS total_customers,
    SUM(churned)                                                  AS total_churned,
    ROUND(SUM(churned) * 100.0 / COUNT(*), 1)                    AS churn_rate_pct,
    ROUND((1 - SUM(churned) * 1.0 / COUNT(*)) * 100, 1)          AS retention_rate_pct
FROM banking_customers;

-- 2. Churn by Account Type
SELECT
    account_type,
    COUNT(*)                                                       AS total_customers,
    SUM(churned)                                                   AS churned,
    ROUND(SUM(churned) * 100.0 / COUNT(*), 1)                     AS churn_rate_pct
FROM banking_customers
GROUP BY account_type
ORDER BY churn_rate_pct DESC;

-- 3. Churn by Number of Products
SELECT
    num_products,
    COUNT(*)                                                       AS customers,
    SUM(churned)                                                   AS churned,
    ROUND(SUM(churned) * 100.0 / COUNT(*), 1)                     AS churn_rate_pct
FROM banking_customers
GROUP BY num_products
ORDER BY num_products;

-- 4. High-Risk Customer Segment
SELECT
    customer_id, age, account_type,
    credit_score, balance, months_active,
    num_transactions_6m, churned
FROM banking_customers
WHERE credit_score        < 600
  AND num_transactions_6m < 5
  AND months_active       < 12
ORDER BY credit_score ASC;

-- 5. Retained vs Churned — Comparison
SELECT
    CASE WHEN churned = 1 THEN 'Churned' ELSE 'Retained' END      AS customer_status,
    COUNT(*)                                                        AS count,
    ROUND(AVG(balance), 0)                                         AS avg_balance,
    ROUND(AVG(credit_score), 0)                                    AS avg_credit_score,
    ROUND(AVG(num_transactions_6m), 1)                             AS avg_txns_6m,
    ROUND(AVG(months_active), 1)                                   AS avg_months_active
FROM banking_customers
GROUP BY churned;
