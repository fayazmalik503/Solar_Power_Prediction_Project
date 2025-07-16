import pandas as pd
import joblib

# Load saved model
model = joblib.load('models/solar_lr_model.joblib')

# Sample input (change values as needed)
sample = pd.DataFrame({
    'Temperature': [34],
    'Humidity': [50],
    'Wind_Speed': [3],
    'Cloud_Cover': [15],
    'UV_Index': [8]
})

# Predict
prediction = model.predict(sample)
print(f"⚡ Predicted Power Output: {prediction[0]:.2f} units")
