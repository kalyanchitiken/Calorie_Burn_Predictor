import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Calorie Burn Prediction - EDA",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Load the dataset
df = pd.read_csv("balanc_diet (1).csv")

st.title("📊 Balanced Diet Dataset - EDA Dashboard")

# Create all-in-one matplotlib figure
fig, axes = plt.subplots(3, 2, figsize=(15, 18))
fig.suptitle('Exploratory Data Analysis on Balanced Diet Dataset', fontsize=16)

# 1. Age Distribution
axes[0, 0].hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Count')

# 2. Gender Distribution
df['Gender'].value_counts().plot(kind='bar', color='coral', edgecolor='black', ax=axes[0, 1])
axes[0, 1].set_title('Gender Distribution')
axes[0, 1].set_xlabel('Gender')
axes[0, 1].set_ylabel('Count')

# 3. Working Type Distribution
df['Working_Type'].value_counts().plot(kind='bar', color='mediumseagreen', edgecolor='black', ax=axes[1, 0])
axes[1, 0].set_title('Working Type Distribution')
axes[1, 0].set_xlabel('Working Type')
axes[1, 0].set_ylabel('Count')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Sleep Hours Distribution
axes[1, 1].hist(df['Sleep_Hours'].dropna(), bins=30, color='violet', edgecolor='black')
axes[1, 1].set_title('Sleep Hours Distribution')
axes[1, 1].set_xlabel('Sleep Hours')
axes[1, 1].set_ylabel('Count')

# 5. Calories vs. Age (Scatter)
axes[2, 0].scatter(df['Age'], df['Required_Daily_Calories'], alpha=0.5, color='teal')
axes[2, 0].set_title('Calories vs. Age')
axes[2, 0].set_xlabel('Age')
axes[2, 0].set_ylabel('Required Daily Calories')

# 6. Correlation Heatmap
corr = df.select_dtypes(include=['float64']).corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Heatmap')

st.pyplot(fig)



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
