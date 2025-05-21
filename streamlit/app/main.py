import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, compute_summary_stats

# Page configuration
st.set_page_config(page_title="Solar Radiation Dashboard", layout="wide")

# Title and Introduction
st.title("📊 Solar Radiation Data Explorer")
st.write("Analyze trends across Benin, Togo, and Sierra Leone with interactive charts.")

# Sidebar for user interaction
country = st.sidebar.selectbox("Select Country", ["Benin", "Togo", "Sierra Leone"])
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Load data dynamically (placeholder for real dataset integration)
df = load_data(country)  

# Display summary statistics
st.subheader("📈 Summary Statistics")
stats_df = compute_summary_stats(df)
st.dataframe(stats_df)

# Interactive Boxplot
st.subheader("📊 Metric Comparison Across Countries")
fig_box = px.box(df, y=metric, color="Country", title=f"{metric} Distribution by Country")
st.plotly_chart(fig_box, use_container_width=True)

# Ranked Table of Top Regions
st.subheader("🏆 Top Regions by Average GHI")
top_regions = df.groupby("Country")[metric].mean().reset_index().sort_values(by=metric, ascending=False)
st.dataframe(top_regions)
