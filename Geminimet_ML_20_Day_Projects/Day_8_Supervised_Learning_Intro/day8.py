# Day 8: Intro to Supervised Learning – Linear & Logistic Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("output.csv")

# Encode 'Passed' column to binary
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# ✅ Linear Regression: Predict Score from Age
X_lr = df[['Age']]
y_lr = df['Score']

X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.25, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train_lr, y_train_lr)
pred_lr = lr_model.predict(X_test_lr)

print("📈 Linear Regression – Predicting Score from Age")
print("Mean Squared Error:", mean_squared_error(y_test_lr, pred_lr))

# Plotting the regression line
plt.figure(figsize=(7, 5))
plt.scatter(X_test_lr, y_test_lr, color='blue', label='Actual')
plt.plot(X_test_lr, pred_lr, color='red', linewidth=2, label='Predicted')
plt.title("Linear Regression: Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("linear_regression.png")
plt.show()

# ✅ Logistic Regression: Predict Pass/Fail from Score
X_log = df[['Score']]
y_log = df['Passed']

X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X_log, y_log, test_size=0.25, random_state=42)

log_model = LogisticRegression()
log_model.fit(X_train_log, y_train_log)
pred_log = log_model.predict(X_test_log)

print("\n📊 Logistic Regression – Predicting Pass/Fail from Score")
print("Accuracy:", accuracy_score(y_test_log, pred_log))
print("Classification Report:\n", classification_report(y_test_log, pred_log))

