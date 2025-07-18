# Streamlit and required libraries import karo
import streamlit as st
import pandas as pd
import joblib

# 🔁 Model load karo from saved path
model_path = r"C:\Users\Fayaz Ahmed Malik\OneDrive\Desktop\Solar_Power_Prediction_Project\models\linear_regression_model.pkl"
model = joblib.load(model_path)

# 🖥️ App ka title
st.title("🔆 Solar Power Prediction Dashboard")

# 📋 User input section ka heading
st.subheader("Enter Weather Data:")

# 🔢 Weather input fields user se lo
temperature = st.number_input("🌡️ Temperature (°C)", value=25.0)
humidity = st.number_input("💧 Humidity (%)", value=50.0)
wind_speed = st.number_input("🌬️ Wind Speed (km/h)", value=10.0)
cloud_cover = st.number_input("☁️ Cloud Cover (%)", value=30.0)
uv_index = st.number_input("🔆 UV Index", value=5.0)

# 🔘 Jab button press ho to prediction karo
if st.button("🔮 Predict Power Output"):
    # 📦 Input values ko DataFrame mein convert karo (model ko aise hi chahiye)
    input_df = pd.DataFrame([[temperature, humidity, wind_speed, cloud_cover, uv_index]],
                            columns=['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'UV_Index'])

    # 🔮 Prediction karo
    prediction = model.predict(input_df)[0]

    # ✅ Result show karo
    st.success(f"⚡ Predicted Power Output: {prediction:.2f} kWh")
