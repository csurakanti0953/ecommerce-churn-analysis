import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Title
st.title("🛍️ E-commerce Churn Dashboard")

# Load the RFM dataset (you must replace this path with your real one)
@st.cache_data(ttl=3600)
def load_data():
    return pd.read_csv("data/processed_rfm.csv")

# Load and clean data
df_raw = load_data()
df_raw.columns = df_raw.columns.str.strip().str.lower()

# Convert timestamp column to datetime (simulate if needed)
df_raw["order_purchase_timestamp"] = pd.to_datetime("2023-01-01") + pd.to_timedelta(
    np.random.randint(0, 180, df_raw.shape[0]), unit="d"
)

# Calculate recency and monetary value
latest_date = df_raw["order_purchase_timestamp"].max()
df = df_raw.groupby("customer_unique_id").agg({
    "order_purchase_timestamp": lambda x: (latest_date - x.max()).days,
    "payment_value": "sum"
}).reset_index()
df.rename(columns={"order_purchase_timestamp": "recency", "payment_value": "monetary"}, inplace=True)

# Add frequency
frequency_df = df_raw.groupby("customer_unique_id").size().reset_index(name="frequency")
df = pd.merge(df, frequency_df, on="customer_unique_id")

# Churn Settings
st.sidebar.header("⚙️ Churn Settings")
threshold = st.sidebar.slider("Churn Recency Threshold (days)",
    min_value=int(df["recency"].min()),
    max_value=int(df["recency"].max()),
    value=int(df["recency"].quantile(0.75))
)
df["churn"] = df["recency"].apply(lambda x: 1 if x > threshold else 0).astype(str)
st.write(f"📏 Churn threshold set to: `{threshold}` days of inactivity")

# Filter Data Sidebar
st.sidebar.header("📊 Filter Data")
min_recency = int(df["recency"].min())
max_recency = int(df["recency"].max())
if min_recency == max_recency:
    max_recency += 1
recency_range = st.sidebar.slider("Recency (days)", min_recency, max_recency, (min_recency, max_recency))
filtered_df = df[(df["recency"] >= recency_range[0]) & (df["recency"] <= recency_range[1])]

# Visualization 1: Recency Distribution
st.subheader("📉 Recency vs Churn")
fig1 = px.histogram(filtered_df, x="recency", color="churn", nbins=40, title="Recency Distribution by Churn")
st.plotly_chart(fig1)

# Visualization 2: Frequency vs Churn
st.subheader("📦 Frequency vs Churn")
fig2 = px.box(filtered_df, x="churn", y="frequency", color="churn", title="Frequency by Churn Status")
st.plotly_chart(fig2)

# Visualization 3: Monetary vs Churn
st.subheader("💰 Monetary Value vs Churn")
fig3 = px.violin(filtered_df, x="churn", y="monetary", color="churn", box=True, points="all",
                 title="Spending Distribution by Churn")
st.plotly_chart(fig3)

# Summary
st.markdown("---")
st.write("📌 Customers with high **recency** and low **frequency** are more likely to churn.")

st.markdown("## 📊 Summary Stats")
st.write(f"🧾 Total customers: {df.shape[0]}")
st.write(f"🔥 Churn rate: {round((df['churn'] == '1').mean() * 100, 2)}%")

# Churn breakdown
st.write("Churned Customers Breakdown:")
st.write(df["churn"].value_counts().rename(index={"1": "Churned", "0": "Retained"}))

# Optional: Download filtered data
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Filtered Data", data=csv, file_name="filtered_customers.csv", mime="text/csv")
