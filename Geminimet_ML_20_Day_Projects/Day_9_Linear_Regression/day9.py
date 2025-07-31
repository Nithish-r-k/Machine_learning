# Day 9: Advanced Linear Regression – Multiple Features + Evaluation

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("output.csv")

# Encode 'Passed' column to binary
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features and Target
X = df[['Age', 'Passed']]  # Multiple independent variables
y = df['Score']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Evaluation
print("📈 Advanced Linear Regression Results")
print("R² Score:", r2_score(y_test, predictions))
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))

# Coefficients
print("\n📊 Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")
print("Intercept:", model.intercept_)

# Residual Plot
residuals = y_test - predictions
plt.figure(figsize=(7, 5))
plt.scatter(predictions, residuals, color='darkorange')
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel("Predicted Score")
plt.ylabel("Residuals")
plt.title("Residual Plot: Predicted vs Residuals")
plt.tight_layout()
plt.savefig("residual_plot.png")
plt.show()

