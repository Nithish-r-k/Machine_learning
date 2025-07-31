# Day 5: Data Cleaning and Preprocessing with Pandas

import pandas as pd

# Load the consistent dataset
df = pd.read_csv("output.csv")
print("📥 Original Data:\n", df)

# 1. Check for Missing Values
print("\n🔍 Missing Values:\n", df.isnull().sum())

# 2. Rename Columns (already renamed from Day 4, shown for clarity)
print("\n📝 Column Names:\n", df.columns)

# 3. Replace 'Passed' from Yes/No back to Boolean if needed
df['Passed'] = df['Passed'].replace({"Yes": True, "No": False})

# 4. Convert Age to Integer (if float)
df['Age'] = df['Age'].astype(int)
print("\n🔢 Converted Age to Integer:\n", df.dtypes)

# 5. Filter: Students who failed
failed_students = df[df['Passed'] == False]
print("\n❌ Students Who Failed:\n", failed_students)

# 6. Save the cleaned output to the same consistent file name
df.to_csv("output.csv", index=False)
print("\n📤 Cleaned data saved again to 'output.csv'")
