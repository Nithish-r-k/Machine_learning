# Day 18: K-Means Clustering – Unsupervised Grouping

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("output.csv")

# Convert 'Passed' to binary for reference (not used in clustering)
df['Passed_Encoded'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features for clustering
X = df[['Score', 'Age']]

# Apply K-Means (2 clusters)
kmeans = KMeans(n_clusters=2, random_state=18, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)

# Centroids
centroids = kmeans.cluster_centers_

# Print results
print(" Cluster Assignments:\n", df[['Name', 'Score', 'Age', 'Cluster']])
print("\n Centroids (Score, Age):\n", centroids)

# Plot clusters
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x='Score', y='Age', hue='Cluster', palette='Set2', s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, color='black', marker='X', label='Centroids')
plt.title("K-Means Clustering of Students")
plt.xlabel("Score")
plt.ylabel("Age")
plt.legend()
plt.tight_layout()
plt.savefig("kmeans_clusters.png")
plt.show()
