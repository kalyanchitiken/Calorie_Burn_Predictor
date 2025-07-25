import streamlit as st
import pandas as pd
import plotly.express as px

# App configuration
st.set_page_config(
    page_title="Calorie Burn EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("📊 Calorie Burn EDA Dashboard")
st.markdown("Explore and visualize the calorie burn dataset using interactive charts.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(balanc_diet (1).csv)
    return df

df = load_data()

# Show dataset
st.subheader("🧾 Dataset Preview")
st.dataframe(df.head())

# Dataset shape
st.markdown(f"**Shape of Dataset:** {df.shape[0]} rows × {df.shape[1]} columns")

# Descriptive statistics
st.subheader("📌 Summary Statistics")
st.write(df.describe())

# Gender Distribution
st.subheader("🔍 Gender Distribution")
gender_count = df['Gender'].value_counts()
fig_gender = px.pie(names=gender_count.index, values=gender_count.values, title="Gender Proportion")
st.plotly_chart(fig_gender, use_container_width=True)

# Working Type Distribution
st.subheader("🧠 Working Type Distribution")
fig_work = px.histogram(df, x="Working_Type", color="Gender", barmode="group", title="Working Type by Gender")
st.plotly_chart(fig_work, use_container_width=True)

# Scatter plot: Age vs Calories
st.subheader("📈 Age vs Required Daily Calories")
fig_age = px.scatter(df, x="Age", y="Required_Daily_Calories", color="Gender",
                     title="Age vs Required Daily Calories")
st.plotly_chart(fig_age, use_container_width=True)

# Scatter plot: Sleep vs Calories
st.subheader("😴 Sleep Hours vs Required Daily Calories")
fig_sleep = px.scatter(df, x="Sleep_Hours", y="Required_Daily_Calories", color="Working_Type",
                       title="Sleep Hours vs Required Daily Calories")
st.plotly_chart(fig_sleep, use_container_width=True)

# Histogram: Calories Distribution
st.subheader("🔥 Required Daily Calories Distribution")
fig_cal = px.histogram(df, x="Required_Daily_Calories", nbins=30, color="Gender",
                       title="Distribution of Daily Calories Burned")
st.plotly_chart(fig_cal, use_container_width=True)

# Correlation matrix
st.subheader("📊 Correlation Heatmap")
numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr(numeric_only=True)
st.dataframe(corr.style.background_gradient(cmap='Blues'), use_container_width=True)
