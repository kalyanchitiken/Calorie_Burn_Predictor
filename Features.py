import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calorie Burn Prediction - Features",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Feature Selection", divider="blue")

st.subheader("What is Feature Selection?")
st.write("""
When building a prediction model, we don't always need every single column from our dataset.  
Some columns may not help at all — they might confuse the model or slow things down.  
**Feature selection** means picking only the most useful columns (features) that help the model give better and faster results.
""")

st.subheader("Why It Matters?")
st.write("""
- Removes unnecessary noise from data  
- Speeds up the training process  
- Reduces chances of overfitting  
- Helps improve accuracy  
""")

st.subheader("How Did We Choose Features?")
st.write("""
We used a technique called **mutual_info_regression**.  
It checks how closely each input (like height, age, sleep hours) is related to the number of calories burned.  
The more related they are, the more useful they are for the model.
""")

# Load your feature importance file
    df = pd.read_csv("mi.csv")
    st.dataframe(df)

    st.subheader("✅ Final Selected Features:")
    st.write("""
    Based on the scores, we kept only the features that were truly helping the model predict better.
    For example:
    - We may have removed a column like **Gender** or **Working_Type** if it wasn't strongly related to calories burned.
    - We kept things like **Height**, **Age**, and **Sleep Hours** because they showed high importance.
    """)
except:
    st.warning("Feature scores file (mi.csv) not found. Please make sure it’s in the root folder.")

st.subheader("Conclusion")
st.write("""
Choosing the right features is like choosing the right ingredients in cooking.  
Even if you have many ingredients, not all are needed.  
The right combination makes the best recipe — or in this case, the best model.
""")