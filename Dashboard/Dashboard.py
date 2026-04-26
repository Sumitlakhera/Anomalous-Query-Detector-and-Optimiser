import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Query Anomaly Detection & Optimization Dashboard",
    layout="wide"
)

st.title("🚀 ML-Based Query Anomaly Detection & Autonomous Optimization")

anomalies = pd.read_csv("anomalies.csv")
opt = pd.read_csv("ai_optimizer_results.csv")
all_queries = pd.read_csv("df_real.csv")



total_queries = len(all_queries)
total_anomalies = anomalies['anomaly_flag'].sum()
optimized_count = len(opt)
avg_improvement = ((opt['improvement']>0).mean())*100
total_saved_time = opt['improvement'].sum()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Queries", total_queries)
c2.metric("Anomalies Detected", int(abs(total_anomalies)))
c3.metric("Optimized Queries", optimized_count)
c4.metric("Improvement Rate", f"{avg_improvement:.2f}%")
c5.metric("Total Time Saved", f"{total_saved_time:.2f}")

st.subheader("📈 Execution Time of Anomalous Queries")

fig, ax = plt.subplots()
ax.hist(anomalies[anomalies['anomaly_flag'] == -1]['execution_time'], bins=25)
ax.set_xlabel("Execution Time")
ax.set_ylabel("Count")
st.pyplot(fig)

st.subheader("📉 Execution Time of Optimized Queries")

fig_opt, ax_opt = plt.subplots()
ax_opt.hist(opt['optimized_time'], bins=25)
ax_opt.set_xlabel("Optimized Execution Time")
ax_opt.set_ylabel("Count")
st.pyplot(fig_opt)

st.subheader("📦 Query Performance Before vs After AI Optimization")

fig_box, ax_box = plt.subplots()

ax_box.boxplot(
    [opt["original_time"], opt["optimized_time"]],
    labels=["Original", "Optimized"]
)

ax_box.set_title("Query Performance Before vs After AI Optimization")
ax_box.set_ylabel("Execution Time (seconds)")

st.pyplot(fig_box)



st.subheader("🧠 Root Cause Breakdown")
st.bar_chart(anomalies['root_cause'].value_counts())

st.subheader("🐌 Top Slow Queries")

slow = anomalies.sort_values("execution_time", ascending=False).head(10)
st.dataframe(
    slow[['query_text','execution_time','complexity_score','scan_ratio','root_cause']]
)

st.subheader("⚡ Optimization Effectiveness")

fig2, ax2 = plt.subplots()
ax2.scatter(opt['original_time'], opt['optimized_time'])
ax2.plot(
    [0, opt['original_time'].max()],
    [0, opt['original_time'].max()],
    linestyle='--'
)
ax2.set_xlabel("Original Time")
ax2.set_ylabel("Optimized Time")
st.pyplot(fig2)

st.subheader("🏆 Highest Performance Gains")

best = opt.sort_values("improvement", ascending=False).head(10)
st.dataframe(
    best[['original_query','original_time','optimized_query','optimized_time','improvement']]
)

st.subheader("🔍 Explore Anomalies by Complexity")

complexity_range = st.slider(
    "Complexity Score",
    float(anomalies['complexity_score'].min()),
    float(anomalies['complexity_score'].max()),
    (
        float(anomalies['complexity_score'].min()),
        float(anomalies['complexity_score'].max())
    )
)

filtered = anomalies[
    (anomalies['complexity_score'] >= complexity_range[0]) &
    (anomalies['complexity_score'] <= complexity_range[1])
]

st.dataframe(filtered)
