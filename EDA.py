import streamlit as st
import pandas as pd
import plotly.express as px

# App config
st.set_page_config(page_title="📊 Calorie Burn EDA", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("balanc_diet (1).csv")

df = load_data()

# Title
st.title("📊 Calorie Burn EDA Dashboard")
st.markdown("Explore and visualize the dataset without shaking charts!")

# Dataset Preview
with st.expander("🔍 Show Dataset Preview"):
    st.dataframe(df.head(), use_container_width=True)

# Dataset Info
col1, col2 = st.columns(2)
col1.metric("Total Rows", df.shape[0])
col2.metric("Total Columns", df.shape[1])

# Summary Stats
st.subheader("📌 Summary Statistics")
st.dataframe(df.describe(), use_container_width=True)

# Gender Distribution Pie
st.subheader("👩‍🦰 Gender Distribution")
fig_gender = px.pie(df, names='Gender', title="Gender Proportion")
st.plotly_chart(fig_gender, use_container_width=True)

# Working Type by Gender - Bar Plot
st.subheader("👨‍💼 Working Type by Gender")
fig_working = px.histogram(df, x="Working_Type", color="Gender", barmode="group")
st.plotly_chart(fig_working, use_container_width=True)

# Box Plot: Required Calories by Gender
st.subheader("📦 Required Calories by Gender")
fig_box = px.box(df, x="Gender", y="Required_Daily_Calories", color="Gender")
st.plotly_chart(fig_box, use_container_width=True)

# Violin Plot: Sleep Hours by Working Type
st.subheader("🎻 Sleep Hours by Working Type")
fig_violin = px.violin(df, x="Working_Type", y="Sleep_Hours", color="Working_Type", box=True, points="all")
st.plotly_chart(fig_violin, use_container_width=True)

# Calories Histogram
st.subheader("🔥 Required Calories Distribution")
fig_hist = px.histogram(df, x="Required_Daily_Calories", nbins=30, color="Gender")
st.plotly_chart(fig_hist, use_container_width=True)

# Correlation Heatmap (static style)
st.subheader("📊 Correlation Heatmap")
corr = df.select_dtypes(include='number').corr(numeric_only=True)
st.dataframe(corr.style.background_gradient(cmap="Blues"), use_container_width=True)
