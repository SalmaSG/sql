# filepath: python_basics.py
"""
Python Basics - A comprehensive introduction to Python programming
This file contains practical examples covering all fundamental concepts.
"""

# =============================================================================
# SECTION 1: YOUR FIRST PYTHON PROGRAM
# =============================================================================

def hello_world():
    """The classic first program in any language."""
    print("Hello, World!")


# =============================================================================
# SECTION 2: VARIABLES AND DATA TYPES
# =============================================================================

def demonstrate_variables():
    """Demonstrate variable declaration and basic data types."""
    # String
    name = "Alice"
    print(f"Name: {name} (type: {type(name).__name__})")
    
    # Integer
    age = 25
    print(f"Age: {age} (type: {type(age).__name__})")
    
    # Float
    height = 5.6
    print(f"Height: {height} (type: {type(height).__name__})")
    
    # Boolean
    is_student = True
    print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
    
    # None
    empty_value = None
    print(f"Empty Value: {empty_value} (type: {type(empty_value).__name__})")


def demonstrate_type_conversion():
    """Demonstrate type conversion between basic types."""
    x = 5
    
    print(f"Original: {x} (type: {type(x).__name__})")
    print(f"int(): {int(x)}")
    print(f"float(): {float(x)}")
    print(f"str(): {str(x)}")
    
    y = "10"
    print(f"\nString '{y}' to int: {int(y)}")
    
    z = 3.7
    print(f"Float {z} to int: {int(z)} (truncates)")


# =============================================================================
# SECTION 3: CONTROL FLOW
# =============================================================================

def demonstrate_if_else():
    """Demonstrate if-elif-else statements."""
    age = 18
    
    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    else:
        print("You are a child")
    
    # Ternary operator
    status = "Adult" if age >= 18 else "Minor"
    print(f"Status: {status}")


def demonstrate_for_loop():
    """Demonstrate for loops with different scenarios."""
    # Iterating over a range
    print("Range iteration:")
    for i in range(5):
        print(f"  {i}", end=" ")
    print()
    
    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    print("\nList iteration:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # Using enumerate
    print("\nWith enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")


def demonstrate_while_loop():
    """Demonstrate while loops."""
    count = 0
    print("While loop:")
    while count < 5:
        print(f"  {count}", end=" ")
        count += 1
    print()


def demonstrate_loop_control():
    """Demonstrate break and continue."""
    print("Break example (stops at 3):")
    for i in range(5):
        if i == 3:
            break
        print(f"  {i}", end=" ")
    print()
    
    print("\nContinue example (skips 2):")
    for i in range(5):
        if i == 2:
            continue
        print(f"  {i}", end=" ")
    print()


# =============================================================================
# SECTION 4: FUNCTIONS
# =============================================================================

def greet(name):
    """Simple greeting function."""
    return f"Hello, {name}!"


def greet_with_default(name="World"):
    """Function with default parameter."""
    return f"Hello, {name}!"


def calculate(a, b, operation="add"):
    """Calculator function with multiple operations."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    return "Unknown operation"


def sum_all(*args):
    """Function accepting variable number of arguments."""
    return sum(args)


def print_info(**kwargs):
    """Function accepting keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# =============================================================================
# SECTION 5: DATA STRUCTURES
# =============================================================================

def demonstrate_lists():
    """Demonstrate list operations."""
    # Creating a list
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    
    # Accessing elements
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # Modifying lists
    fruits.append("date")
    fruits.insert(1, "avocado")
    fruits.remove("banana")
    print(f"Modified fruits: {fruits}")
    
    # Slicing
    print(f"numbers[1:4]: {numbers[1:4]}")
    print(f"numbers[:3]: {numbers[:3]}")
    print(f"numbers[::2]: {numbers[::2]}")
    
    # List comprehension
    squares = [x**2 for x in range(5)]
    print(f"Squares: {squares}")


def demonstrate_tuples():
    """Demonstrate tuple operations."""
    # Creating a tuple
    point = (10, 20)
    colors = ("red", "green", "blue")
    
    # Accessing elements
    print(f"Point x: {point[0]}")
    
    # Unpacking
    x, y = point
    print(f"Unpacked: x={x}, y={y}")
    
    # Tuple with single element
    single = (5,)
    print(f"Single element tuple: {single}")


def demonstrate_dictionaries():
    """Demonstrate dictionary operations."""
    # Creating a dictionary
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    
    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Email: {person.get('email', 'Not provided')}")
    
    # Modifying dictionary
    person["age"] = 26
    person["email"] = "alice@example.com"
    
    # Iterating
    print("\nDictionary items:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}
    print(f"Square dictionary: {squares}")


def demonstrate_sets():
    """Demonstrate set operations."""
    # Creating a set
    fruits = {"apple", "banana", "cherry", "apple"}
    print(f"Set (duplicates removed): {fruits}")
    
    # Adding/removing elements
    fruits.add("date")
    fruits.remove("banana")
    print(f"After modifications: {fruits}")
    
    # Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"Union: {set1.union(set2)}")
    print(f"Intersection: {set1.intersection(set2)}")
    print(f"Difference (set1 - set2): {set1.difference(set2)}")


# =============================================================================
# SECTION 6: PRACTICE EXERCISES
# =============================================================================

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def simple_calculator():
    """Simple calculator using functions."""
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b): return a / b if b != 0 else "Error"
    
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide)
    }
    
    print("\n--- Simple Calculator ---")
    print("Select operation: 1-Add 2-Subtract 3-Multiply 4-Divide")
    
    choice = input("Enter choice: ")
    if choice in operations:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            name, func = operations[choice]
            result = func(a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input!")
    else:
        print("Invalid choice!")


def count_word_frequency(text):
    """Count word frequency in a text."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON BASICS DEMONSTRATION")
    print("=" * 60)
    
    # Section 1: Hello World
    print("\n--- Section 1: Hello World ---")
    hello_world()
    
    # Section 2: Variables
    print("\n--- Section 2: Variables and Data Types ---")
    demonstrate_variables()
    demonstrate_type_conversion()
    
    # Section 3: Control Flow
    print("\n--- Section 3: Control Flow ---")
    demonstrate_if_else()
    demonstrate_for_loop()
    demonstrate_while_loop()
    demonstrate_loop_control()
    
    # Section 4: Functions
    print("\n--- Section 4: Functions ---")
    print(greet("Alice"))
    print(greet_with_default())
    print(greet_with_default("Bob"))
    print(f"Calculate 10 + 5: {calculate(10, 5, 'add')}")
    print(f"Calculate 10 * 5: {calculate(10, 5, 'multiply')}")
    print(f"Sum all: {sum_all(1, 2, 3, 4, 5)}")
    print("\nKwargs:")
    print_info(name="Alice", age=25, city="New York")
    
    # Section 5: Data Structures
    print("\n--- Section 5: Data Structures ---")
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sets()
    
    # Section 6: Practice Exercises
    print("\n--- Section 6: Practice Exercises ---")
    print("Prime number check:")
    for n in [1, 2, 3, 4, 5, 17, 18, 19]:
        print(f"  {n} is prime: {is_prime(n)}")
    
    print("\nWord frequency count:")
    text = "python python is fun python programming is fun"
    freq = count_word_frequency(text)
    print(f"  Text: '{text}'")
    print(f"  Frequency: {freq}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)