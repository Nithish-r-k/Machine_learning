# Day 15: Naive Bayes Classification

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("output.csv")

# Encode Passed column
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features and Target
X = df[['Score', 'Age']]
y = df['Passed']

# Train full model (small dataset)
model = GaussianNB()
model.fit(X, y)
y_pred = model.predict(X)

# Evaluation
print("🧠 Naive Bayes Classification Results")
print("Accuracy:", accuracy_score(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))

# Plot confusion matrix
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d', cmap='BuPu',
            xticklabels=['Pred No', 'Pred Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title("Naive Bayes – Confusion Matrix")
plt.tight_layout()
plt.savefig("naive_bayes_confusion_matrix.png")
plt.show()
