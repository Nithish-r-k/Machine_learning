# Day 19: Comparing Classifier Performance

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("output.csv")
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

X = df[['Score', 'Age']]
y = df['Passed']

# Models to compare
models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(kernel='linear')
}

results = []

for name, model in models.items():
    model.fit(X, y)
    preds = model.predict(X)
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y, preds),
        "Precision": precision_score(y, preds, zero_division=0),
        "Recall": recall_score(y, preds, zero_division=0),
        "F1 Score": f1_score(y, preds, zero_division=0)
    })

# Convert to DataFrame
results_df = pd.DataFrame(results)
print("📊 Model Evaluation Summary:\n")
print(results_df)

# Plot
plt.figure(figsize=(10, 6))
for metric in ["Accuracy", "Precision", "Recall", "F1 Score"]:
    plt.plot(results_df["Model"], results_df[metric], marker='o', label=metric)
plt.title("Model Comparison Metrics")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.ylim(0, 1.1)
plt.legend()
plt.tight_layout()
plt.savefig("model_comparison_chart.png")
plt.show()

