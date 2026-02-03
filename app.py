import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Trader Performance vs Market Sentiment",
    layout="wide"
)

st.title("📊 Trader Performance vs Market Sentiment")
st.write(
    "This dashboard explores how Fear and Greed market sentiment "
    "affects trader behavior and performance on Hyperliquid."
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/daily_metrics.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Market Sentiment",
    options=df["sentiment_bucket"].unique(),
    default=df["sentiment_bucket"].unique()
)

df = df[df["sentiment_bucket"].isin(sentiment_filter)]

# -------------------------------
# Chart 1: PnL by Sentiment
# -------------------------------
st.subheader("Daily PnL Distribution by Market Sentiment")

fig1, ax1 = plt.subplots()
sns.boxplot(
    data=df,
    x="sentiment_bucket",
    y="daily_pnl",
    ax=ax1
)
ax1.set_xlabel("Market Sentiment")
ax1.set_ylabel("Daily PnL")
st.pyplot(fig1)

# -------------------------------
# Chart 2: Risk Bucket vs PnL
# -------------------------------
st.subheader("Daily PnL by Risk Bucket")

fig2, ax2 = plt.subplots()
sns.boxplot(
    data=df,
    x="risk_bucket",
    y="daily_pnl",
    hue="sentiment_bucket",
    ax=ax2
)
ax2.set_xlabel("Risk Bucket")
ax2.set_ylabel("Daily PnL")
st.pyplot(fig2)

# -------------------------------
# Chart 3: Trader Clusters
# -------------------------------
if "cluster" in df.columns:
    st.subheader("Trader Behavioral Clusters")

    fig3, ax3 = plt.subplots()
    sns.countplot(
        data=df,
        x="cluster",
        ax=ax3
    )
    ax3.set_xlabel("Cluster")
    ax3.set_ylabel("Number of Trader-Days")
    st.pyplot(fig3)

# -------------------------------
# Data Preview
# -------------------------------
st.subheader("Data Preview")
st.dataframe(df.head(20))

st.write(
    "🔍 This lightweight dashboard is intended for exploratory analysis "
    "and complements the detailed findings in the notebook."
)
