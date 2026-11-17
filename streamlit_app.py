import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("predictor.pkl")

def predict_price(crim, zn, indus, nox, rm, age, dis, tax, ptratio, lstat):
    features = np.array([[crim, zn, indus, nox, rm, age, dis, tax, ptratio, lstat]])
    prediction = model.predict(features)
    return prediction[0]

# Page configuration
st.set_page_config(page_title="Boston Housing Price Predictor", page_icon="??", layout="wide")

# Styling
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("?? Boston Housing Price Predictor")
st.write("Enter the housing data in the sidebar to predict the price.")

# Sidebar for inputs
with st.sidebar:
    st.header("Housing Features")
    crim = st.number_input("CRIM (Crime Rate)", value=0.1)
    zn = st.number_input("ZN (Residential Land Zoned)", value=0.0)
    indus = st.number_input("INDUS (Non-Retail Business)", value=5.0)
    nox = st.number_input("NOX (Nitric Oxides)", value=0.5)
    rm = st.number_input("RM (Average Rooms)", value=6.0)
    age = st.number_input("AGE (Proportion Built Before 1940)", value=50.0)
    dis = st.number_input("DIS (Distance to Employment Centers)", value=4.0)
    tax = st.number_input("TAX (Property Tax Rate)", value=300.0)
    ptratio = st.number_input("PTRATIO (Pupil-Teacher Ratio)", value=15.0)
    lstat = st.number_input("LSTAT (% Lower Status)", value=10.0)

# Prediction button in main area
if st.button("Predict Price", type="primary"):
    price = predict_price(crim, zn, indus, nox, rm, age, dis, tax, ptratio, lstat)
    st.metric(label="Predicted Housing Price", value=f"${price:.2f}k")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Made for Boston Housing Model</p>
</div>
""", unsafe_allow_html=True)
