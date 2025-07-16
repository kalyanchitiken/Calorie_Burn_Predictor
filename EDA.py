import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calorie Burn Prediction - EDA",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Exploratory Data Analysis", divider="blue")

st.subheader("🧾 Statistics")
st.write("""
The dataset contains information about people’s age, gender, height, sleep habits, and working type.  
Our goal is to understand how these features relate to the number of calories they burn.
""")

# Load your dataset
df = pd.read_csv("balanc_diet (1).csv")  # adjust filename if different
st.dataframe(df.head())

st.subheader("📊 Quick Summary")
st.write(df.describe())

st.subheader("📌 Observations")
st.write("""
- **Age** ranges from teenagers to older adults.
- **Gender** is labeled as 0 or 1 (probably Female and Male).
- **Working_Type** includes different job roles like Private, Government, etc.
- **Sleep_Hours** is usually between 5 to 9 hours per night.
- **Height_m** varies from short to tall individuals.
- **Calories_Burned** is our target, and it seems to increase with height and age.
""")

st.subheader("🔍 Correlation Check")
st.write("""
Let’s look at how features relate to calories burned.

- **Age**: Older people tend to burn more.
- **Height**: Taller people burn more calories.
- **Sleep Hours**: There’s a slight trend—more rest may affect calorie usage.
- **Working Type**: Certain jobs seem to involve more physical activity.

""")

st.subheader("📈 Visualizations")

# Images are placed in Images folder (place your .png files there)
col1, col2 = st.columns(2)
with col1:
    st.image("Images/correlation_heatmap.png", caption="Correlation Heatmap", use_column_width=True)

with col2:
    st.image("Images/sleep_vs_calories.png", caption="Sleep Hours vs Calories Burned", use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    st.image("Images/height_vs_calories.png", caption="Height vs Calories Burned", use_column_width=True)

with col2:
    st.image("Images/workingtype_distribution.png", caption="Working Type Distribution", use_column_width=True)

st.subheader("🧠 Key Takeaways")
st.write("""
- People who are taller and older generally burn more calories.
- Job type matters — more active jobs lead to more calorie burn.
- Sleep plays a small but noticeable role.
- Most people fall in the mid-range for calories burned, but a few outliers exist with very high values.
""")
