# Day 13: Decision Tree Classifier

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("output.csv")

# Encode target
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features and target
X = df[['Score', 'Age']]
y = df['Passed']

# Train model on full dataset (since it’s small)
model = DecisionTreeClassifier(criterion='entropy', random_state=13)
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Evaluation
print("📊 Decision Tree Evaluation")
print("Accuracy:", accuracy_score(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))

# Plot confusion matrix
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d', cmap='YlGnBu',
            xticklabels=['Pred No', 'Pred Yes'], yticklabels=['Actual No', 'Actual Yes'])
plt.title("Decision Tree – Confusion Matrix")
plt.tight_layout()
plt.savefig("decision_tree_confusion_matrix.png")
plt.show()

# Plot the decision tree
plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=['Score', 'Age'], class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree Structure")
plt.tight_layout()
plt.savefig("decision_tree_structure.png")
plt.show()

