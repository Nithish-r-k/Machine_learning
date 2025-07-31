# Day 10: Polynomial Regression – Nonlinear Curve Fitting

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("output.csv")

# Use Age to predict Score
X = df[['Age']].values
y = df['Score'].values

# Apply Polynomial Features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train the model
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)

# Evaluate model
print("📈 Polynomial Regression Evaluation")
print("R² Score:", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))

# Visualize polynomial curve
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Actual')
# Sort X for smooth curve plotting
sort_idx = np.argsort(X[:, 0])
X_sorted = X[sort_idx]
y_sorted_pred = model.predict(poly.transform(X_sorted))
plt.plot(X_sorted, y_sorted_pred, color='red', linewidth=2, label='Predicted (Poly Fit)')
plt.title("Polynomial Regression: Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("polynomial_regression.png")
plt.show()

