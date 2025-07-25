import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv(balanc_diet (1).csv)  # Ensure this file exists in root
    return df

def app():
    st.title("Exploratory Data Analysis")

    df = load_data()

    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Calories vs Age")
    fig1 = px.scatter(df, x="Age", y="Required_Daily_Calories", color="Gender")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Calories vs Sleep Hours")
    fig2 = px.scatter(df, x="Sleep_Hours", y="Required_Daily_Calories", color="Working_Type")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Height vs Calories")
    fig3 = px.scatter(df, x="Height_m", y="Required_Daily_Calories", color="Gender")
    st.plotly_chart(fig3, use_container_width=True)
