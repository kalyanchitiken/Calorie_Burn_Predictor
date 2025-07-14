import streamlit as st

st.set_page_config(
    page_title="Calorie Burn Prediction",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.header("Calorie Burn Prediction App", divider="green")

st.subheader("📌 What is this App About?")
st.write("""
This project aims to estimate the number of calories a person burns based on simple personal and lifestyle factors such as:
- Age
- Gender
- Work Type
- Sleep Hours
- Height

🔥 Predicting calorie burn is helpful for:
- Personal fitness tracking
- Weight loss planning
- Health monitoring
- Diet recommendations
""")

st.subheader("🔍 How Does the App Work?")
st.write("""
- This is a **regression project** using a trained machine learning model.
- The model is trained using a dataset that contains age, gender, sleep hours, etc., and their corresponding calorie burn.
- The app takes your input and instantly predicts the **estimated calories burned** using the trained model (`calorie_model.pkl`).
""")

st.markdown("---")

st.subheader("👨‍💻 About Me")
st.write("""
---
### About Me
Hi, I'm **Kalyan Chitiken**, a data science enthusiast from Hyderababd,India 
This app was developed as part of my ML learning and deployment journey.

📧 Email: kalyanchitiken@gmail.com  
🔗 LinkedIn: [Kalyan Chitiken] www.linkedin.com/in/kalyan-chitiken-a16480217

""")