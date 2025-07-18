# ☀️ Solar Power Output Prediction

This project aims to predict solar power output using weather data for Karachi. It leverages multiple regression models to estimate future energy generation, helping solar energy companies optimize their output planning.

---

## 📌 Objective

- **Use Case:** Assist solar companies in forecasting daily solar energy production.
- **Goal:** Predict **Power Output** based on historical weather features such as temperature, humidity, wind speed, etc.
- **Location:** Karachi
- **Timeframe:** 180 days of historical data

---

## 📊 Dataset Information

- **Source:** Kaggle (public dataset)
- **Total Records:** 180 rows
- **Columns:**

| Column        | Description                        |
|---------------|------------------------------------|
| `Date`        | Daily recorded date                |
| `Temperature` | Temperature in Celsius             |
| `Humidity`    | Humidity percentage                |
| `Wind_Speed`  | Wind speed in m/s                  |
| `Cloud_Cover` | Cloud coverage percentage          |
| `UV_Index`    | Ultraviolet index                  |
| `Power_Output`| Generated solar power (target var) |

---

## 📈 Exploratory Data Analysis (EDA)

- ✅ No missing values in the dataset
- 🔍 Pairplot and distribution analysis for feature insight
- 📊 Correlation Matrix:
  - `UV_Index` shows strong correlation with `Power_Output` (0.80)
  - `Cloud_Cover` has negative correlation (-0.46)

<div align="center">
  <img src="cb8a7328-a86c-4c64-bae8-f8cd2c3e7354.png" alt="EDA Results" width="700"/>
</div>

---

## 🤖 Models & Evaluation

Several regression models were trained and evaluated using MAE and RMSE:

| Model                     | MAE    | RMSE   |
|---------------------------|--------|--------|
| **Linear Regression**     | 38.95  | 46.60  |
| Ridge Regression          | 38.99  | 46.65  |
| Decision Tree             | 57.32  | 72.65  |
| Random Forest             | 51.00  | 64.30  |
| Gradient Boosting         | 51.28  | 66.29  |
| Support Vector Regression | 129.34 | 158.68 |

> 🔥 **Best Performing Model:** Linear Regression

---

## 🧠 Final Model

- **Selected:** Linear Regression
- **Reason:** Lowest MAE & RMSE among all tested models
- **Saved with:** `joblib` in VS Code for later use

---

## 📦 Tools & Libraries

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook
- VS Code

---

## 🔍 Prediction Sample

```python
import joblib
model = joblib.load("linear_model.pkl")
sample = [[30, 45, 7, 20, 6]]  # Example input: [Temp, Humidity, Wind, Cloud, UV]
prediction = model.predict(sample)
print(f"Predicted Power Output: {prediction[0]:.2f}")

