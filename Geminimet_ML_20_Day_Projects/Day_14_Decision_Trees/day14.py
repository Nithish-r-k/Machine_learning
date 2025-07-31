# Day 14: Random Forest Classifier

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("output.csv")

# Encode Passed column
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features and Target
X = df[['Score', 'Age']]
y = df['Passed']

# Train full model (tiny dataset)
model = RandomForestClassifier(n_estimators=100, random_state=14)
model.fit(X, y)
y_pred = model.predict(X)

# Evaluation
print("🌲 Random Forest Classifier Evaluation")
print("Accuracy:", accuracy_score(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))

# Plot confusion matrix
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d', cmap='YlOrBr',
            xticklabels=['Pred No', 'Pred Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title("Random Forest – Confusion Matrix")
plt.tight_layout()
plt.savefig("random_forest_confusion_matrix.png")
plt.show()

# Feature Importance
plt.figure(figsize=(6, 4))
importances = model.feature_importances_
features = ['Score', 'Age']
sns.barplot(x=importances, y=features, palette='viridis')
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.savefig("random_forest_feature_importance.png")
plt.show()
