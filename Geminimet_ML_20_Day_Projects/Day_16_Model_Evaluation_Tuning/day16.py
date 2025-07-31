# Day 16: Support Vector Machine (SVM) Classifier

import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("output.csv")

# Encode target
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features and Target
X = df[['Score', 'Age']]
y = df['Passed']

# Train SVM model on full dataset
model = SVC(kernel='linear', C=1.0)
model.fit(X, y)
y_pred = model.predict(X)

# Evaluation
print("⚔️ SVM Classification Results")
print("Accuracy:", accuracy_score(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))

# Confusion Matrix Visualization
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d', cmap='Blues',
            xticklabels=['Pred No', 'Pred Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title("SVM – Confusion Matrix")
plt.tight_layout()
plt.savefig("svm_confusion_matrix.png")
plt.show()
