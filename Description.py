import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Calorie Burn Prediction",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.header("Dataset Description", divider="blue")

df = pd.read_csv("balanc_diet.csv")  
st.dataframe(df)

# Create two columns
left_col, right_col = st.columns([1.5, 1])

st.subheader("📂 Dataset Overview")
st.write("""This dataset contains details about people’s daily routines, body stats, and lifestyle habits. It's used to understand how different factors like age, height, sleep hours, and working type affect calories burned.

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10200 entries, 0 to 10199
Data columns (total 7 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   ID                       10200 non-null  int64  
 1   Age                      10171 non-null  float64
 2   Gender                   10200 non-null  object 
 3   Working_Type             10171 non-null  object 
 4   Sleep_Hours              10171 non-null  float64
 5   Height_m                 10171 non-null  float64
 6   Required_Daily_Calories  10171 non-null  float64
dtypes: float64(4), int64(1), object(2)
memory usage: 557.9+ KB  

""")
