# Trader Performance vs Market Sentiment (Fear vs Greed)

## Overview
This project analyzes how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and performance on the Hyperliquid platform. By aligning daily market sentiment with trader-level execution data, the analysis uncovers behavioral patterns that can inform smarter, more risk-aware trading strategies.

The focus is on understanding how traders adjust activity, risk exposure, and performance under different sentiment regimes.

---

## Data Sources
1. Bitcoin Fear & Greed Index
   - Columns: Date, Classification (Fear / Greed / Extreme values)
   - Sentiment handling:
     - Fear = Fear + Extreme Fear
     - Greed = Greed + Extreme Greed
     - Neutral was retained separately for reference but excluded from some analyses due to limited signal.

2. Hyperliquid Historical Trader Data
   - Trade-level data including account, side, execution price, trade size, fees, and closed PnL.

---

## Methodology
- Cleaned and validated both datasets (checked missing values and duplicates).
- Converted timestamps to daily granularity and aligned both datasets by date.
- Engineered key daily trader metrics:
  - Daily PnL per account
  - Win rate
  - Average trade size (used as a proxy for leverage)
  - Number of trades per day
  - Long/short ratio
- Compared trader behavior and performance across Fear and Greed regimes.
- Segmented traders based on behavior and performance.
- Added bonus analysis including predictive modeling, clustering, and a lightweight dashboard.

---

## Trader Segmentation
Traders were segmented into the following groups:

- High Risk vs Low Risk Traders  
  Based on average daily trade size as a proxy for leverage.

- Frequent vs Infrequent Traders  
  Based on the number of trades per day relative to the median.

- Consistent vs Inconsistent Traders  
  Based on the volatility of daily PnL over time.

---

Key Insights
- Greed sentiment amplifies both profits and losses, increasing overall risk exposure.
- Frequent trading during Greed leads to higher volatility without consistently better outcomes.
- Consistent traders demonstrate resilience to market sentiment, while inconsistent traders are highly sensitive to Fear and Greed regimes.

All insights are supported by charts and aggregated tables in the analysis notebook.

---

Actionable Strategy Recommendations
1. During "Fear" sentiment, high-risk traders should reduce position sizes and effective leverage, as losses among inconsistent traders are significantly higher.
2. During "Greed" sentiment, only consistent traders should increase trade frequency, as inconsistent traders face elevated volatility and drawdowns despite higher upside.

---

Bonus Analysis
- Predictive Model  
  A simple logistic regression model predicts next-day trader profitability using sentiment and behavioral features. While intentionally lightweight, results show that sentiment-aware behavior contains predictive signal despite class imbalance.

- Trader Clustering 
  Traders were clustered into three behavioral archetypes based on trade frequency, trade size, and win rate, revealing distinct trading styles.

- Streamlit Dashboard 
  A lightweight Streamlit dashboard enables interactive exploration of PnL distributions, risk exposure, and trader clusters.

---

How to Run

1. Clone the repository
```bash
git clone <your-repo-link>
cd primetrade-trader-sentiment
