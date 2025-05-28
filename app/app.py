import streamlit as st
from disease_model import load_model, predict_disease

# Load the trained model
model = load_model('models/trained_models.pkl')

# Streamlit UI
st.title("Fitness Guide: Disease Risk Prediction")
age = st.number_input("Age", min_value=0, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
# Add more input fields as needed

# Predict button
if st.button("Predict Disease Risk"):
    input_data = [age, bmi]  # Add more inputs as needed
    prediction = predict_disease(model, input_data)
    st.write(f"Predicted Disease Risk: {prediction}")
