import streamlit as st

pages = {
    "1️⃣ Introduction":[
        st.Page("Intro.py", title="Introduction & Topic Details"),
    ],
    "2️⃣ Problem + Dataset": [
        st.Page("Problem.py", title="Problem Statement & Objective"),
        st.Page("Description.py", title="Dataset Description"),
        st.Page("EDA.py", title="Exploratory Data Analysis"),
        st.Page("Features.py", title="Feature Selection"),
        st.Page("Model_Building.py", title="Model Building and Evaluation"),
        
    ],
    "3️⃣ Model Section": [
        st.Page("Predict.py", title="Model"),
    ]
}

pg = st.navigation(pages)
pg.run()