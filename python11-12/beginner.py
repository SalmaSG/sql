# filepath: beginner.py
"""
Python Beginner Tutorial - Very Basic Examples
Perfect for absolute beginners starting from zero.
"""

# =============================================================================
# 1. PRINTING - How to show output on screen
# =============================================================================

print("Hello, World!")           # Simple text
print(42)                        # Numbers
print(3.14)                      # Decimals
print(True)                      # True/False

# =============================================================================
# 2. VARIABLES - Storing information
# =============================================================================

# String (text)
name = "John"
print(name)

# Number (integer)
age = 20
print(age)

# Decimal (float)
price = 9.99
print(price)

# True/False (boolean)
is_active = True
print(is_active)

# =============================================================================
# 3. MATH OPERATIONS
# =============================================================================

a = 10
b = 3

print(a + b)     # Addition: 13
print(a - b)     # Subtraction: 7
print(a * b)     # Multiplication: 30
print(a / b)     # Division: 3.333...
print(a // b)    # Whole division: 3
print(a % b)     # Remainder: 1
print(a ** b)    # Power: 1000

# =============================================================================
# 4. COMPARING VALUES
# =============================================================================

x = 5
y = 10

print(x == y)    # Equal: False
print(x != y)   # Not equal: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less or equal: True
print(x >= y)   # Greater or equal: False

# =============================================================================
# 5. SIMPLE IF STATEMENT
# =============================================================================

number = 5

if number > 0:
    print("Positive number")
else:
    print("Negative or zero")

# =============================================================================
# 6. SIMPLE FOR LOOP
# =============================================================================

# Print numbers 0 to 4
for i in range(5):
    print(i)

# Print each letter
word = "Python"
for letter in word:
    print(letter)

# =============================================================================
# 7. SIMPLE WHILE LOOP
# =============================================================================

count = 0
while count < 3:
    print(count)
    count = count + 1

# =============================================================================
# 8. LISTS - Storing multiple items
# =============================================================================

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Get first item
print(fruits[0])

# Get last item
print(fruits[-1])

# Add item
fruits.append("date")
print(fruits)

# =============================================================================
# 9. DICTIONARY - Key-Value pairs
# =============================================================================

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person)
print(person["name"])
print(person["age"])

# =============================================================================
# 10. SIMPLE FUNCTION
# =============================================================================

def say_hello():
    print("Hello!")

def greet(name):
    print("Hello, " + name)

def add(a, b):
    return a + b

# Call functions
say_hello()
greet("Bob")
result = add(3, 4)
print(result)

# =============================================================================
# 11. INPUT - Getting user input
# =============================================================================

# Uncomment to try:
# name = input("Enter your name: ")
# print("Hello, " + name)

# =============================================================================
# 12. COMMENTS - Notes in code
# =============================================================================

# This is a single line comment

"""
This is a
multi-line
comment
"""

# =============================================================================
# END OF BASIC TUTORIAL
# =============================================================================

print("\n--- Tutorial Complete ---")
print("You learned the basics of Python!")
print("Keep practicing to get better.")