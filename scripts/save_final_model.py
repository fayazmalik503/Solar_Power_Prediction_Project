import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Load data
df = pd.read_csv('data/solar_weather.csv')
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])

# Step 2: Select features
features = ['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'UV_Index']
X = df[features]
y = df['Power_Output']

# Step 3: Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Save model
joblib.dump(model, 'models/solar_lr_model.joblib')
print("✅ Linear Regression model saved!")
