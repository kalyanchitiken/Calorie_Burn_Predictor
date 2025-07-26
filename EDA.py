import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Calorie Burn EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("📊 Calorie Burn EDA Dashboard")
st.markdown("This dashboard helps you explore and understand the calorie burn dataset visually.")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("balanc_diet (1).csv")

df = load_data()

# Dataset Preview
st.header("📄 Dataset Overview")
st.dataframe(df.head(), use_container_width=True)
st.markdown(f"✅ **Dataset Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

# Summary Statistics
st.header("📌 Summary Statistics")
st.write(df.describe())

# Gender Distribution (Pie Chart)
st.header("👥 Gender Distribution")
gender_counts = df['Gender'].value_counts()
fig_gender = px.pie(
    names=gender_counts.index,
    values=gender_counts.values,
    title="Proportion of Genders",
    color_discrete_sequence=px.colors.qualitative.Safe
)
st.plotly_chart(fig_gender, use_container_width=True)

# Working Type by Gender (Grouped Bar Chart)
st.header("💼 Working Type by Gender")
fig_worktype = px.histogram(
    df, x='Working_Type', color='Gender', barmode='group',
    title="Working Type Distribution by Gender"
)
st.plotly_chart(fig_worktype, use_container_width=True)

# Age vs Required Calories (Scatter)
st.header("📈 Age vs Required Daily Calories")
fig_age = px.scatter(
    df, x="Age", y="Required_Daily_Calories", color="Gender",
    title="Age vs Required Daily Calories"
)
st.plotly_chart(fig_age, use_container_width=True)

# Sleep vs Calories (Bubble Chart)
st.header("😴 Sleep Hours vs Calories (Bubble Chart)")
fig_sleep = px.scatter(
    df, x="Sleep_Hours", y="Required_Daily_Calories", size="Age",
    color="Working_Type", hover_data=["Gender"],
    title="Calories vs Sleep Hours and Age"
)
st.plotly_chart(fig_sleep, use_container_width=True)

# Height vs Calories (Box Plot)
st.header("📦 Height vs Required Daily Calories")
fig_height = px.box(
    df, x="Gender", y="Height_m", color="Gender",
    title="Height Distribution by Gender"
)
st.plotly_chart(fig_height, use_container_width=True)

# Calories Distribution by Gender (Histogram)
st.header("🔥 Required Daily Calories Distribution by Gender")
fig_cal = px.histogram(
    df, x="Required_Daily_Calories", color="Gender",
    nbins=30, title="Calories Distribution by Gender"
)
st.plotly_chart(fig_cal, use_container_width=True)

# Correlation Heatmap (Static Image using Seaborn)
st.header("🧠 Correlation Heatmap")

# Correlation with numerical columns
numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr(numeric_only=True)

# Plot with seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".2f", ax=ax)
st.pyplot(fig)

# Display correlation matrix as styled table
st.subheader("📋 Correlation Matrix (Table Format)")
st.dataframe(corr.style.background_gradient(cmap='Blues'), use_container_width=True)
