# Day 1: Python Basics

# 1. Greet User Function
def greet_user(name):
    return f"Hello, {name}!"

print(greet_user("Aashu"))

# 2. Print Even Numbers from List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# 3. Student Data Dictionary
student = {
    "name": "Aashutosh",
    "age": 24,
    "course": "Python"
}
print("Student Info:")
for key, value in student.items():
    print(f"{key}: {value}")

# 4. Calculator with Functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return "Cannot divide by zero" if y == 0 else x / y

print("Add:", add(5, 3))
print("Subtract:", subtract(5, 3))
print("Multiply:", multiply(5, 3))
print("Divide:", divide(5, 3))
