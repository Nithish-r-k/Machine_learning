# Day 17: Principal Component Analysis (PCA)

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("output.csv")

# Encode target
df['Passed'] = df['Passed'].replace({'Yes': 1, 'No': 0})

# Features for PCA
X = df[['Score', 'Age']]
y = df['Passed']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA (2 components for visualization)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create PCA DataFrame
pca_df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
pca_df['Passed'] = y

# Variance retained
print("🔎 Explained Variance Ratio:", pca.explained_variance_ratio_)
print("🔢 Total Variance Retained:", sum(pca.explained_variance_ratio_))

# Visualize PCA result
plt.figure(figsize=(7, 5))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Passed', palette={1: "green", 0: "red"}, s=100)
plt.title("PCA Projection (2D)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.tight_layout()
plt.savefig("pca_projection.png")
plt.show()

