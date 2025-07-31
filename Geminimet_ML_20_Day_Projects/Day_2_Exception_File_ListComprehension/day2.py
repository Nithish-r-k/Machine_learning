# Day 2: Exception Handling, File Handling, List Comprehension

# 1. Exception Handling – Division Example

def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero.")
    except ValueError:
        print("❌ Error: Please enter valid integers.")
    else:
        print(f"✅ Result = {result}")
    finally:
        print("✅ Division operation complete.\n")

# Uncomment to run:
# divide_numbers()

# 2. File Handling – Write and Read Example
def write_and_read_file():
    filename = "day2_output.txt"
    
    # Writing to file
    with open(filename, "w") as file:
        file.write("This is Day 2 of ML Project by Nithish.\n")
        file.write("Learning Python File Handling.\n")
    
    # Reading from file
    with open(filename, "r") as file:
        content = file.read()
        print("📄 File Content:\n", content)

write_and_read_file()

# 3. List Comprehension Examples
numbers = list(range(1, 21))

# Square of numbers
squares = [x**2 for x in numbers]
print("🔢 Squares:", squares)

# Even numbers
evens = [x for x in numbers if x % 2 == 0]
print("🟢 Even numbers:", evens)

# Uppercasing characters in a string
chars = [char.upper() for char in "nithish"]
print("🔠 Characters in uppercase:", chars)

# Conditional List – Pass/Fail
marks = [40, 55, 70, 30, 90]
results = ["Pass" if mark >= 50 else "Fail" for mark in marks]
print("🎓 Results:", results)

# Nested List – Multiplication Table
print("\n📊 5x5 Multiplication Table:")
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

