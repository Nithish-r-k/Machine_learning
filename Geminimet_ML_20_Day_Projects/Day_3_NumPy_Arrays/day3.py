# Day 3: NumPy Arrays and Operations

import numpy as np

# 1. Creating Arrays
array1 = np.array([1, 2, 3, 4, 5])
print("📦 1D Array:", array1)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n📦 2D Array:\n", array2)

# 2. Array Properties
print("\n🔍 Array Properties:")
print("Shape:", array2.shape)
print("Size:", array2.size)
print("Data Type:", array2.dtype)

# 3. Array Slicing and Indexing
print("\n🧩 Slicing Examples:")
print("First element:", array1[0])
print("Last two elements:", array1[-2:])
print("Element at (1,2) in 2D array:", array2[1, 2])

# 4. Array Operations
print("\n➕ Mathematical Operations:")
print("Add 10 to every element:", array1 + 10)
print("Multiply by 2:", array1 * 2)

# 5. Matrix Operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\n🧮 Matrix Operations:")
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", A + B)
print("A * B (element-wise):\n", A * B)
print("A dot B (matrix multiplication):\n", A @ B)

# 6. Useful NumPy Functions
print("\n🛠️ Useful NumPy Functions:")
print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((3, 2)))
print("Random numbers:\n", np.random.rand(2, 2))
print("Range from 0 to 10:\n", np.arange(0, 11, 2))
