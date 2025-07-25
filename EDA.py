import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page settings
st.set_page_config(
    page_title="Calorie Burn Prediction - EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("balanc_diet (1).csv")

df = load_data()

st.title("📊 Balanced Diet Dataset - EDA Dashboard")

# -------------------------------------
st.header("📈 Overview Charts")

col1, col2 = st.columns(2)

with col1:
    fig_age = px.histogram(df, x="Age", nbins=30, title="Age Distribution",
                           color_discrete_sequence=['skyblue'])
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    fig_gender = px.bar(df["Gender"].value_counts().reset_index(),
                        x="index", y="Gender", title="Gender Distribution",
                        labels={"index": "Gender", "Gender": "Count"},
                        color_discrete_sequence=['coral'])
    st.plotly_chart(fig_gender, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig_work = px.bar(df["Working_Type"].value_counts().reset_index(),
                      x="index", y="Working_Type", title="Working Type Distribution",
                      labels={"index": "Job Type", "Working_Type": "Count"},
                      color_discrete_sequence=['mediumseagreen'])
    st.plotly_chart(fig_work, use_container_width=True)

with col4:
    fig_sleep = px.histogram(df, x="Sleep_Hours", nbins=30,
                             title="Sleep Hours Distribution",
                             color_discrete_sequence=['violet'])
    st.plotly_chart(fig_sleep, use_container_width=True)

# -------------------------------------
st.header("🔍 Feature Relationships")

col5, col6 = st.columns(2)

with col5:
    fig_cal_age = px.scatter(df, x="Age", y="Required_Daily_Calories",
                             title="Calories vs Age",
                             opacity=0.6, color_discrete_sequence=['teal'])
    st.plotly_chart(fig_cal_age, use_container_width=True)

with col6:
    fig_cal_sleep = px.scatter(df, x="Sleep_Hours", y="Required_Daily_Calories",
                               title="Calories vs Sleep Hours",
                               opacity=0.6, color_discrete_sequence=['orange'])
    st.plotly_chart(fig_cal_sleep, use_container_width=True)

col7, col8 = st.columns(2)

with col7:
    fig_cal_height = px.scatter(df, x="Height_m", y="Required_Daily_Calories",
                                title="Calories vs Height",
                                opacity=0.6, color_discrete_sequence=['green'])
    st.plotly_chart(fig_cal_height, use_container_width=True)

with col8:
    # Correlation heatmap (float columns)
    corr_df = df.select_dtypes(include='number').corr().round(2)
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=corr_df.values,
        x=corr_df.columns,
        y=corr_df.index,
        colorscale='RdBu',
        zmin=-1, zmax=1,
        colorbar=dict(title="Correlation")
    ))
    fig_heatmap.update_layout(title="Correlation Heatmap", xaxis_nticks=36)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# -------------------------------------
st.header("🧾 Dataset Overview")

st.subheader("📊 First 5 Records")
st.dataframe(df.head())

st.subheader("📌 Summary Statistics")
st.dataframe(df.describe())

# -------------------------------------
st.header("🧠 Key Observations")
st.write("""
- Taller and older individuals generally burn more calories.
- Certain working types (more physical jobs) tend to burn more.
- Sleep hours show a mild positive influence on calorie usage.
- Gender and height may contribute indirectly via BMI/physical traits.
""")
