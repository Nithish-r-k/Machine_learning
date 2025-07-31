import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and preprocess data
df = pd.read_csv("output.csv")

# Convert Passed to string explicitly (ensures compatibility with Seaborn)
df['Passed'] = df['Passed'].astype(str)
df['Passed'] = df['Passed'].replace({'True': 'Yes', 'False': 'No'})

# Set theme
sns.set(style="whitegrid")

# 1. Barplot – Name vs Score
plt.figure(figsize=(8, 5))
sns.barplot(x='Name', y='Score', data=df, color='skyblue', errorbar=None)
plt.title("Student Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("seaborn_barplot.png")
plt.show()

# 2. Countplot – Pass vs Fail (Now safely using string-based palette)
plt.figure(figsize=(5, 5))
sns.countplot(x='Passed', data=df, palette={'Yes': 'green', 'No': 'red'})
plt.title("Pass vs Fail Count")
plt.xlabel("Result")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("seaborn_countplot.png")
plt.show()

# 3. Boxplot – Score by Passed
plt.figure(figsize=(7, 5))
sns.boxplot(x='Passed', y='Score', data=df, palette="pastel")
plt.title("Score Distribution by Pass/Fail")
plt.tight_layout()
plt.savefig("seaborn_boxplot.png")
plt.show()

# 4. Scatterplot – Age vs Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Score', data=df, hue='Passed', style='Passed', s=100)
plt.title("Age vs Score with Pass/Fail Hue")
plt.tight_layout()
plt.savefig("seaborn_scatterplot.png")
plt.show()
