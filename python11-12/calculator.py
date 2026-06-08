# filepath: calculator.py
"""
Simple Calculator Program
Performs basic arithmetic operations: +, -, *, /
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    print("Available operations:")
    print("  +  : Addition")
    print("  -  : Subtraction")
    print("  *  : Multiplication")
    print("  /  : Division")
    print("  q  : Quit")
    print("=" * 40)
    
    while True:
        # Get operation from user
        operation = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")
        
        if operation.lower() == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        # Validate operation
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation! Please enter +, -, *, or /")
            continue
        
        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter numeric values.")
            continue
        
        # Perform calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        # Display result
        print(f"Result: {num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()