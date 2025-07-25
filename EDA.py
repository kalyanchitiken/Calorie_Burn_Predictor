import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="EDA", layout="wide")

# Title
st.title("📊 Exploratory Data Analysis - Calorie Burn Prediction")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("calories.csv")  # Replace with actual filename
    return df

df = load_data()

# Show top rows
st.subheader("🔍 Preview of Dataset")
st.dataframe(df.head())

# ------------------------------
# Gender Count Plot
# ------------------------------
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
fig_gender.update_traces(textposition="outside")
st.plotly_chart(fig_gender, use_container_width=True)

# ------------------------------
# Age Distribution
# ------------------------------
st.subheader("🎂 Age Distribution")
fig_age = px.histogram(
    df,
    x="Age",
    color="Gender",
    nbins=20,
    title="Age Distribution by Gender"
)
st.plotly_chart(fig_age, use_container_width=True)

# ------------------------------
# Sleep Hours Distribution
# ------------------------------
st.subheader("😴 Sleep Hours Distribution")
fig_sleep = px.histogram(
    df,
    x="Sleep_Hours",
    color="Gender",
    nbins=20,
    title="Sleep Hours Distribution by Gender"
)
st.plotly_chart(fig_sleep, use_container_width=True)

# ------------------------------
# Required Calories vs Age
# ------------------------------
st.subheader("🔥 Required Daily Calories vs Age")
fig_cal = px.scatter(
    df,
    x="Age",
    y="Required_Daily_Calories",
    color="Gender",
    size="Height_m",
    hover_data=["Working_Type", "Sleep_Hours"],
    title="Calories vs Age"
)
st.plotly_chart(fig_cal, use_container_width=True)

# ------------------------------
# Box Plot: Calories by Working Type
# ------------------------------
st.subheader("💼 Calories by Working Type")
fig_work = px.box(
    df,
    x="Working_Type",
    y="Required_Daily_Calories",
    color="Working_Type",
    title="Calorie Needs Based on Work Type"
)
st.plotly_chart(fig_work, use_container_width=True)

# ------------------------------
# Summary Stats
# ------------------------------
st.subheader("📈 Summary Statistics")
st.write(df.describe())
