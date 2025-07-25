import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit config
st.set_page_config(
    page_title="Calorie Burn Prediction - EDA",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("balanc_diet (1).csv")

df = load_data()

st.title("📊 Balanced Diet Dataset - EDA Dashboard")

# --------------------------------------------
# 👇 All-in-one Overview Plot
@st.cache_data
def draw_combined_plot(df):
    fig, axes = plt.subplots(3, 2, figsize=(15, 18))
    fig.suptitle('Exploratory Data Analysis on Balanced Diet Dataset', fontsize=16)

    # Age Distribution
    axes[0, 0].hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Age Distribution')
    axes[0, 0].set_xlabel('Age')
    axes[0, 0].set_ylabel('Count')

    # Gender Distribution
    df['Gender'].value_counts().plot(kind='bar', color='coral', edgecolor='black', ax=axes[0, 1])
    axes[0, 1].set_title('Gender Distribution')
    axes[0, 1].set_xlabel('Gender')
    axes[0, 1].set_ylabel('Count')

    # Working Type
    df['Working_Type'].value_counts().plot(kind='bar', color='mediumseagreen', edgecolor='black', ax=axes[1, 0])
    axes[1, 0].set_title('Working Type Distribution')
    axes[1, 0].set_xlabel('Working Type')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].tick_params(axis='x', rotation=45)

    # Sleep Hours
    axes[1, 1].hist(df['Sleep_Hours'].dropna(), bins=30, color='violet', edgecolor='black')
    axes[1, 1].set_title('Sleep Hours Distribution')
    axes[1, 1].set_xlabel('Sleep Hours')
    axes[1, 1].set_ylabel('Count')

    # Scatter: Age vs Calories
    axes[2, 0].scatter(df['Age'], df['Required_Daily_Calories'], alpha=0.5, color='teal')
    axes[2, 0].set_title('Calories vs. Age')
    axes[2, 0].set_xlabel('Age')
    axes[2, 0].set_ylabel('Required Daily Calories')

    # Correlation Heatmap
    corr = df.select_dtypes(include=['float64']).corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[2, 1])
    axes[2, 1].set_title('Correlation Heatmap')

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    return fig

st.pyplot(draw_combined_plot(df))

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

# --------------------------------------------
# 👇 Detailed Visualizations

@st.cache_data
def plot_corr_heatmap(data):
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(data.select_dtypes(include=['float64']).corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    fig.tight_layout()
    return fig

@st.cache_data
def plot_sleep_vs_calories(data):
    fig, ax = plt.subplots()
    ax.scatter(data['Sleep_Hours'], data['Required_Daily_Calories'], alpha=0.6, color='orange')
    ax.set_xlabel("Sleep Hours")
    ax.set_ylabel("Required Daily Calories")
    ax.set_title("Sleep vs Calories")
    fig.tight_layout()
    return fig

@st.cache_data
def plot_height_vs_calories(data):
    fig, ax = plt.subplots()
    ax.scatter(data['Height_m'], data['Required_Daily_Calories'], alpha=0.6, color='green')
    ax.set_xlabel("Height (m)")
    ax.set_ylabel("Required Daily Calories")
    ax.set_title("Height vs Calories")
    fig.tight_layout()
    return fig

@st.cache_data
def plot_working_type(data):
    fig, ax = plt.subplots()
    data['Working_Type'].value_counts().plot(kind='bar', ax=ax, color='purple', edgecolor='black')
    ax.set_title("Working Type Distribution")
    ax.set_xlabel("Job Type")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig

col1, col2 = st.columns(2)

with col1:
    st.subheader("Correlation Heatmap")
    st.pyplot(plot_corr_heatmap(df))

with col2:
    st.subheader("Sleep Hours vs Calories Burned")
    st.pyplot(plot_sleep_vs_calories(df))

col3, col4 = st.columns(2)

with col3:
    st.subheader("Height vs Calories Burned")
    st.pyplot(plot_height_vs_calories(df))

with col4:
    st.subheader("Working Type Distribution")
    st.pyplot(plot_working_type(df))

# --------------------------------------------
st.subheader("🧠 Key Takeaways")
st.write("""
- People who are taller and older generally burn more calories.
- Job type matters — more active jobs lead to more calorie burn.
- Sleep plays a small but noticeable role.
- Most people fall in the mid-range for calories burned, but a few outliers exist with very high values.
""")
