import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load(r'C:\Users\Fayaz Ahmed Malik\OneDrive\Desktop\solar-power-project\models.joblib')
st.title("Solar Power Prediction App")

temperature = st.number_input("Enter Temperature (°C)")
humidity = st.number_input("Enter Humidity (%)")
wind_speed = st.number_input("Enter Wind Speed (km/h)")
cloud_cover = st.number_input("Enter Cloud Cover (%)")
uv_index = st.number_input("Enter UV Index")

if st.button("Predict Power Output"):
    input_data = pd.DataFrame([[temperature, humidity, wind_speed, cloud_cover, uv_index]],
                              columns=['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'UV_Index'])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Power Output: {prediction:.2f} kW")