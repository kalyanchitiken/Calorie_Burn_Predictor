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

# All-in-one plot (6 subplots)
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

# 6. Correlation Heatmap (small version)
corr = df.select_dtypes(include=['float64']).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[2, 1])
axes[2, 1].set_title('Correlation Heatmap')

# Show all-in-one plot
st.pyplot(fig)

# --------------------------------------------

st.header("Exploratory Data Analysis", divider="blue")

st.subheader("🧾 Statistics")
st.write("""
The dataset contains information about people’s age, gender, height, sleep habits, and working type.  
Our goal is to understand how these features relate to the number of calories they burn.
""")

st.subheader("📊 Quick Summary")
st.dataframe(df.head())
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

st.subheader("📈 Visualizations (Detailed)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Correlation Heatmap")
    corr = df.select_dtypes(include=['float64']).corr()
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax1)
    st.pyplot(fig1)

with col2:
    st.subheader("Sleep Hours vs Calories Burned")
    fig2, ax2 = plt.subplots()
    ax2.scatter(df['Sleep_Hours'], df['Required_Daily_Calories'], alpha=0.6, color='orange')
    ax2.set_xlabel("Sleep Hours")
    ax2.set_ylabel("Required Daily Calories")
    ax2.set_title("Sleep vs Calories")
    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Height vs Calories Burned")
    fig3, ax3 = plt.subplots()
    ax3.scatter(df['Height_m'], df['Required_Daily_Calories'], alpha=0.6, color='green')
    ax3.set_xlabel("Height (m)")
    ax3.set_ylabel("Required Daily Calories")
    ax3.set_title("Height vs Calories")
    st.pyplot(fig3)

with col4:
    st.subheader("Working Type Distribution")
    fig4, ax4 = plt.subplots()
    df['Working_Type'].value_counts().plot(kind='bar', ax=ax4, color='purple', edgecolor='black')
    ax4.set_title("Working Type Distribution")
    ax4.set_xlabel("Job Type")
    ax4.set_ylabel("Count")
    st.pyplot(fig4)

st.subheader("🧠 Key Takeaways")
st.write("""
- People who are taller and older generally burn more calories.
- Job type matters — more active jobs lead to more calorie burn.
- Sleep plays a small but noticeable role.
- Most people fall in the mid-range for calories burned, but a few outliers exist with very high values.
""")
