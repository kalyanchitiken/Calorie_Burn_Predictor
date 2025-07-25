import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="EDA", layout="wide")

# Title
st.title("📊 Exploratory Data Analysis - Calorie Burn Prediction")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("balanc_diet (1).csv")  # Replace with your actual dataset name/path
    return df

df = load_data()

# Show sample of data
st.subheader("🔍 Preview of Dataset")
st.dataframe(df.head())

# Gender Distribution
st.subheader("🧍 Gender Distribution")
gender_counts = df["Gender"].value_counts().reset_index()
gender_counts.columns = ["Gender", "Count"]
fig_gender = px.bar(
    gender_counts,
    x="Gender",
    y="Count",
    color="Gender",
    title="Gender Distribution",
    text="Count"
)
fig_gender.update_traces(textposition='outside')
st.plotly_chart(fig_gender, use_container_width=True)

# Age Distribution
st.subheader("🎂 Age Distribution")
fig_age = px.histogram(
    df,
    x="Age",
    nbins=30,
    color="Gender",
    title="Distribution of Age by Gender"
)
st.plotly_chart(fig_age, use_container_width=True)

# Duration vs Calories Burned
st.subheader("🔥 Duration vs Calories Burned")
fig_calories = px.scatter(
    df,
    x="Duration",
    y="Calories",
    color="Gender",
    size="Age",
    hover_data=["Age"],
    title="Calories Burned vs Duration of Exercise"
)
st.plotly_chart(fig_calories, use_container_width=True)

# Heart Rate Distribution
if "Heart_Rate" in df.columns:
    st.subheader("❤️ Heart Rate Distribution")
    fig_heart = px.histogram(df, x="Heart_Rate", nbins=30, title="Heart Rate Distribution")
    st.plotly_chart(fig_heart, use_container_width=True)

# Summary Stats
st.subheader("📈 Summary Statistics")
st.write(df.describe())
