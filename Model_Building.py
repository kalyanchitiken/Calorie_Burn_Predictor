import streamlit as st

st.set_page_config(
    page_title="Calorie Burn Prediction App",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.header("Model Building", divider="blue")

# What is Model Building
st.subheader("What is Model Building?")
st.write("""
Model building in machine learning is the process of training a predictive model using existing data. 
It includes selecting the right algorithm, preparing the data, training the model, and evaluating its performance. 
The goal is to learn patterns from historical data so the model can accurately predict outcomes for new, unseen inputs.
""")

# Which model to use
st.subheader("Which Model to Use?")
st.write("""
### Nature of the Problem:
- The target variable is **Calories Burned**, which is a **continuous** value.
- This makes it a **regression problem**, not classification.

### Model Comparison:
- **Naive Bayes** is mainly used for classification tasks (e.g., spam detection, disease prediction).
- **K-Nearest Neighbors (KNN)** supports both **classification and regression**.

### Conclusion:
- **KNN Regressor (KNeighborsRegressor)** is the better choice for predicting calorie burn.
- It works well with simple lifestyle features like **Age, Gender, Working Type, Sleep Hours, and Height**.
- Naive Bayes is not suitable here unless we convert the regression task into a classification task (e.g., Low/Medium/High calories), which reduces accuracy and flexibility.
""")