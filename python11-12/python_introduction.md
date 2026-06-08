# Python Introduction

Welcome to Python programming! This guide will help you get started with the fundamentals of Python.

## Table of Contents
1. [What is Python?](#what-is-python)
2. [Your First Python Program](#your-first-python-program)
3. [Variables and Data Types](#variables-and-data-types)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Data Structures](#data-structures)

---

## What is Python?

Python is a high-level, interpreted programming language known for its readability and versatility. It was created by Guido van Rossum and first released in 1991.

### Key Features:
- **Easy to Learn** - Simple syntax that reads like English
- **Versatile** - Used for web development, data science, AI, automation, and more
- **Cross-Platform** - Works on Windows, Mac, and Linux
- **Large Community** - Extensive libraries and resources available

---

## Your First Python Program

The classic first program in any language is "Hello, World!"

```python
# filepath: hello_world.py
print("Hello, World!")
```

To run this program:
```bash
python hello_world.py
```

---

## Variables and Data Types

### Variables

Variables are containers for storing data values. In Python, you don't need to declare the type explicitly.

```python
# filepath: variables.py
name = "Alice"        # String
age = 25              # Integer
height = 5.6          # Float
is_student = True     # Boolean

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")
```

### Basic Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `10`, `-3` | Whole numbers |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `str` | `"Hello"`, `'Python'` | Text/characters |
| `bool` | `True`, `False` | Logical values |
| `None` | `None` | Empty/null value |

### Type Conversion

```python
# filepath: type_conversion.py
# Convert between types
x = 5
print(int(x))      # 5
print(float(x))    # 5.0
print(str(x))      # "5"

y = "10"
print(int(y))     # 10

z = 3.7
print(int(z))     # 3 (truncates)
```

---

## Control Flow

### If-Else Statements

```python
# filepath: conditionals.py
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
print(status)
```

### Loops

#### For Loop

```python
# filepath: for_loop.py
# Iterating over a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### While Loop

```python
# filepath: while_loop.py
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control

```python
# filepath: loop_control.py
# Break - exit loop completely
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue - skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

---

## Functions

Functions are reusable blocks of code that perform a specific task.

### Defining Functions

```python
# filepath: functions.py
def greet(name):
    """This function greets a person."""
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)

# Default parameters
def greet_with_default(name="World"):
    return f"Hello, {name}!"

print(greet_with_default())        # Hello, World!
print(greet_with_default("Bob"))   # Hello, Bob!
```

### Multiple Parameters

```python
# filepath: function_params.py
def add(a, b):
    return a + b

def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"

print(calculate(10, 5, "add"))       # 15
print(calculate(10, 5, "multiply"))   # 50
```

### *args and **kwargs

```python
# filepath: args_kwargs.py
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
```

---

## Data Structures

### Lists

Lists are ordered, mutable collections.

```python
# filepath: lists.py
# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(fruits[0])    # apple
print(fruits[-1])   # cherry (last element)

# Modifying lists
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")

# Slicing
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[::2])   # [1, 3, 5] (every other element)

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### Tuples

Tuples are ordered, immutable collections.

```python
# filepath: tuples.py
# Creating a tuple
point = (10, 20)
colors = ("red", "green", "blue")

# Accessing elements
print(point[0])   # 10

# Unpacking
x, y = point
print(f"x: {x}, y: {y}")

# Tuple with single element (note the comma)
single = (5,)  # Not (5)
```

### Dictionaries

Dictionaries store key-value pairs.

```python
# filepath: dictionaries.py
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])      # Alice
print(person.get("email", "Not provided"))  # Not provided

# Modifying dictionary
person["age"] = 26
person["email"] = "alice@example.com"

# Iterating
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sets

Sets are unordered collections of unique elements.

```python
# filepath: sets.py
# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # duplicates removed

# Adding/removing elements
fruits.add("date")
fruits.remove("banana")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}
```

---

## Next Steps

Now that you've learned the basics, here are some topics to explore next:

1. **File I/O** - Reading and writing files
2. **Error Handling** - Try/except blocks
3. **Object-Oriented Programming** - Classes and objects
4. **Modules and Packages** - Organizing code
5. **Working with Libraries** - pip and virtual environments

### Practice Exercises

1. Write a function that checks if a number is prime
2. Create a simple calculator using functions
3. Build a to-do list application using lists
4. Write a program that counts word frequency in a text

---

*Happy Coding! 🚀*