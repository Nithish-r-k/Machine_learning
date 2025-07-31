# Day 11: Logistic Regression – Binary Classification

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("output.csv")

# Encode Passed column
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Feature and Target
X = df[['Score']]
y = df['Passed']

# Train and predict on full dataset
model = LogisticRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Evaluation
print("📊 Logistic Regression Evaluation")
print("Accuracy:", accuracy_score(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))

# Plot Confusion Matrix
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d', cmap='Blues',
            xticklabels=['Pred No', 'Pred Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("logistic_confusion_matrix.png")
plt.show()
