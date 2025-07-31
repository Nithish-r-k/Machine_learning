
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("output.csv")

# 1. Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Score'], color='skyblue')
plt.title("Test Scores by Student")
plt.xlabel("Student")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# 2. Pie Chart – Passed vs Failed
pass_counts = df['Passed'].value_counts()
labels = pass_counts.index
colors = ['green', 'red']
plt.figure(figsize=(5, 5))
plt.pie(pass_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pass vs Fail Distribution")
plt.savefig("pie_chart.png")
plt.show()

# 3. Line Plot – Age vs Score
plt.figure(figsize=(8, 5))
plt.plot(df['Age'], df['Score'], marker='o', linestyle='-', color='purple')
plt.title("Age vs Test Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.grid(True)
plt.tight_layout()
plt.savefig("line_plot.png")
plt.show()

# 4. Histogram – Distribution of Scores
plt.figure(figsize=(8, 5))
plt.hist(df['Score'], bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Test Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()



