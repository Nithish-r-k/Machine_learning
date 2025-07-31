
# day20.py – Full Train + Save + Predict Capstone Script

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# --- Training & Saving Model ---
df = pd.read_csv("output.csv")
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})
X = df[['Score', 'Age']]
y = df['Passed']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
joblib.dump(model, 'model.pkl')
print(" Model trained and saved as model.pkl")

# --- Loading Model & Predicting ---
model = joblib.load("model.pkl")
print(" Model loaded successfully")

# Sample input
score = 82
age = 22

input_data = pd.DataFrame([[score, age]], columns=["Score", "Age"])
prediction = model.predict(input_data)[0]

print("\n Student Info:")
print(f"Score: {score} | Age: {age}")
print("\n Prediction Result:")
print("🎓 Passed " if prediction == 1 else " Failed ")
