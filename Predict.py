import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from imblearn.pipeline import Pipeline   
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,f1_score,precision_score,confusion_matrix,classification_report
from imblearn.over_sampling import SMOTE
import streamlit as st
import pickle

st.title("Calorie Burn Prediction App")

st.subheader("Enter Transaction Details Below")

age = st.number_input("Enter your age :",min_value=10,max_value=100)
gender = st.selectbox("Gender :", ["Male", "Female", "Other"])
working_type = st.selectbox("Working Type:",["Freelancer","Private","Government","Self-employed","Others"])
sleep_hours = st.slider("Sleep Hours", 0.0, 24.0, step=0.1, value=7.0)
Height_m = st.number_input("Height (in meters)", 1.0, 2.5, step=0.01)

input_df = pd.DataFrame([[age, gender, working_type, sleep_hours, Height_m]],
                        columns=['Age', 'Gender', 'Working_Type', 'Sleep_Hours', 'Height_m'])  


with open("colories.pkl","rb") as f:
    model = pickle.load(f)

if st.button("submit the details"):
    pred = model.predict(input_df)
    st.write(f" Predicted Calories Burned: {pred[0]:.2f}")