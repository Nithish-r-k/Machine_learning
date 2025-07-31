# Day 12: K-Nearest Neighbors Classifier

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("output.csv")

# Encode 'Passed' column to binary
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features and target
X = df[['Score', 'Age']]
y = df['Passed']

# Skip split for small dataset
X_train, X_test = X, X
y_train, y_test = y, y


# Create KNN model (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Evaluation
print("📊 KNN Classification Results")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Plot confusion matrix
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='BuGn',
            xticklabels=['Pred No', 'Pred Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title("KNN – Confusion Matrix")
plt.tight_layout()
plt.savefig("knn_confusion_matrix.png")
plt.show()

