import streamlit as st

st.set_page_config(
    page_title="Calorie Prediction App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("Problem Statement", divider="orange")

st.write("With rising awareness about health and fitness, many people want to know how many calories they burn each day. But manually calculating calories based on age, sleep, height, or job type is difficult and time-consuming. There's no one-size-fits-all formula because every person is different.")

st.subheader("Objective")

st.write("""
The goal of this project is to build a simple and smart machine learning model that predicts how many calories a person is likely to burn based on a few personal details like:

- Age  
- Gender  
- Working type  
- Sleep hours  
- Height_meter

This prediction system can help users:  
✅ Keep better track of their daily health and habits
✅ Know how much energy they’re using throughout the day
✅ Get helpful tips on how to balance food, sleep, and activity
✅ Make smarter choices to stay fit, active, and feel good

""")
