# Day 4: Pandas – DataFrames and Analysis

import pandas as pd

# 1. Create DataFrame from Dictionary
data = {
    'Name': ['Nithi', 'Kavi', 'Mahi', 'Vinoj'],
    'Age': [22, 23, 24, 21],
    'Score': [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print("📊 DataFrame:\n", df)

# 2. Accessing Columns
print("\n🔍 Names Column:\n", df['Name'])

# 3. Basic Statistics
print("\n📈 Statistical Summary:\n", df.describe())

# 4. Adding a New Column
df['Passed'] = df['Score'] >= 80
print("\n✅ Updated DataFrame:\n", df)

# 5. Filtering Rows
high_scorers = df[df['Score'] > 85]
print("\n🎯 Students with Score > 85:\n", high_scorers)

# 6. Reading CSV (Simulated Inline Example)
# In real case: df = pd.read_csv('students.csv')
print("\n📁 Simulated CSV Read Complete.")

# 7. Indexing and Slicing
print("\n🔢 First Two Rows:\n", df.iloc[:2])
print("\n🧩 Name and Score Columns:\n", df[['Name', 'Score']])

# 8. Exporting to CSV
df.to_csv("day4_output.csv", index=False)
print("\n📤 DataFrame saved to 'day4_output.csv'")

