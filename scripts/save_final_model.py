import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

print("📂 Step 1: Loading data...")

# Load data
df = pd.read_csv(r"C:\Users\Fayaz Ahmed Malik\OneDrive\Desktop\Solar_Power_Prediction_Project\data\solar_weather.csv")
df = df.dropna()

print("📊 Step 2: Preparing features and target...")

# Features & target
X = df[['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'UV_Index']]
y = df['Power_Output']

print("✂️ Step 3: Splitting data...")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🧠 Step 4: Training model...")

# Train model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

print("💾 Step 5: Saving model...")

# Save path
model_folder = r"C:\Users\Fayaz Ahmed Malik\OneDrive\Desktop\Solar_Power_Prediction_Project\models"
if not os.path.exists(model_folder):
    os.makedirs(model_folder)

model_save_path = os.path.join(model_folder, "linear_regression_model.pkl")

# Try saving
try:
    joblib.dump(lr_model, model_save_path)
    print("✅ Model saved successfully at:", model_save_path)
except Exception as e:
    print("❌ Error while saving model:", e)