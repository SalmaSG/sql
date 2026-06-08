"""
Python Demo: Iterators, Modules, Date & Math
Comprehensive examples covering three key Python concepts
"""

# ============================================================================
# 1. ITERATORS
# ============================================================================
print("=" * 70)
print("1. ITERATORS - Custom and Built-in")
print("=" * 70)

# Basic Iterator Concept
print("\n--- Iter() and Next() ---")
my_list = [10, 20, 30, 40]
my_iterator = iter(my_list)

print(f"Original list: {my_list}")
print(f"Get first item: {next(my_iterator)}")
print(f"Get second item: {next(my_iterator)}")
print(f"Get third item: {next(my_iterator)}")
print(f"Get fourth item: {next(my_iterator)}")

# Custom Iterator Class
print("\n--- Custom Iterator Class ---")
class CountUp:
    """Custom iterator that counts up to a specified number"""
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUp(5)
print("Counting from 1 to 5:")
for num in counter:
    print(f"  {num}", end=" ")
print()

# Iterator from String
print("\n--- Iterator from String ---")
my_string = "Python"
string_iterator = iter(my_string)
print(f"String: {my_string}")
print("Characters:", [next(string_iterator) for _ in range(3)])

# Generator Function (simplest iterator)
print("\n--- Generator Function ---")
def fibonacci_generator(limit):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers < 100:")
fib = fibonacci_generator(100)
print(list(fib))

# ============================================================================
# 2. MODULES
# ============================================================================
print("\n" + "=" * 70)
print("2. MODULES - Built-in and Custom")
print("=" * 70)

# Random Module
print("\n--- Random Module ---")
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Random choice from {numbers}: {random.choice(numbers)}")
print(f"Random sample (3 items): {random.sample(numbers, 3)}")
print(f"Random number 1-100: {random.randint(1, 100)}")
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# Collections Module
print("\n--- Collections Module ---")
from collections import Counter, deque
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word counts: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# Double-ended queue
queue = deque([1, 2, 3])
queue.append(4)
queue.appendleft(0)
print(f"Deque operations: {queue}")

# OS Module
print("\n--- OS Module ---")
import os
print(f"Current directory: {os.getcwd()}")
print(f"Platform: {os.name}")
print(f"Path separator: {os.sep}")

# Sys Module
print("\n--- Sys Module ---")
import sys
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

# Custom Module Example
print("\n--- Custom Module (Calculator Functions) ---")
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
    return a / b if b != 0 else "Cannot divide by zero"

print(f"20 + 5 = {add(20, 5)}")
print(f"20 - 5 = {subtract(20, 5)}")
print(f"20 * 5 = {multiply(20, 5)}")
print(f"20 / 5 = {divide(20, 5)}")

# ============================================================================
# 3. DATE & TIME
# ============================================================================
print("\n" + "=" * 70)
print("3. DATE & TIME - DateTime Module")
print("=" * 70)

from datetime import datetime, timedelta, date, time

# Current Date and Time
print("\n--- Current Date & Time ---")
now = datetime.now()
print(f"Current date & time: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

# Date Only
print("\n--- Date Only ---")
today = date.today()
print(f"Today's date: {today}")
print(f"Formatted: {today.strftime('%d-%m-%Y')}")

# Time Only
print("\n--- Time Only ---")
current_time = time(14, 30, 45)
print(f"Time: {current_time}")

# Creating Specific Dates
print("\n--- Creating Specific Dates ---")
birthday = datetime(2000, 5, 15, 10, 30)
print(f"Birthday: {birthday}")

# Date Arithmetic
print("\n--- Date Arithmetic with TimeDelta ---")
future_date = now + timedelta(days=7)
past_date = now - timedelta(weeks=2)
print(f"Today: {now.date()}")
print(f"7 days from now: {future_date.date()}")
print(f"2 weeks ago: {past_date.date()}")

# Days between dates
print("\n--- Days Between Dates ---")
date1 = datetime(2026, 5, 18)
date2 = datetime(2026, 6, 15)
difference = date2 - date1
print(f"From {date1.date()} to {date2.date()}: {difference.days} days")

# Formatting Dates
print("\n--- Date Formatting ---")
print(f"Default: {now}")
print(f"US Format: {now.strftime('%m/%d/%Y')}")
print(f"European Format: {now.strftime('%d.%m.%Y')}")
print(f"With time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Full text: {now.strftime('%A, %B %d, %Y')}")

# Parse Date String
print("\n--- Parse Date from String ---")
date_string = "2026-12-25"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed: {parsed_date}")

# ============================================================================
# 4. MATH MODULE
# ============================================================================
print("\n" + "=" * 70)
print("4. MATH - Mathematical Functions")
print("=" * 70)

import math

# Basic Math Operations
print("\n--- Basic Math Operations ---")
print(f"Absolute value of -15: {abs(-15)}")
print(f"Power (2^5): {pow(2, 5)}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")

# Trigonometric Functions
print("\n--- Trigonometric Functions ---")
angle = math.radians(45)  # Convert degrees to radians
print(f"sin(45°): {math.sin(angle):.4f}")
print(f"cos(45°): {math.cos(angle):.4f}")
print(f"tan(45°): {math.tan(angle):.4f}")

# Logarithmic Functions
print("\n--- Logarithmic Functions ---")
print(f"log(100, base 10): {math.log10(100)}")
print(f"log(8, base 2): {math.log2(8)}")
print(f"Natural log of e: {math.log(math.e):.4f}")

# Constants
print("\n--- Mathematical Constants ---")
print(f"Pi (π): {math.pi}")
print(f"Euler's number (e): {math.e}")
print(f"Tau (2π): {math.tau}")
print(f"Infinity: {math.inf}")

# Factorial
print("\n--- Factorial ---")
print(f"5! = {math.factorial(5)}")
print(f"10! = {math.factorial(10)}")

# GCD and LCM
print("\n--- GCD (Greatest Common Divisor) ---")
print(f"GCD(48, 18): {math.gcd(48, 18)}")

# Degrees and Radians Conversion
print("\n--- Degree/Radian Conversion ---")
degrees = 180
radians = math.radians(degrees)
print(f"{degrees}° = {radians:.4f} radians")
print(f"{radians:.4f} radians = {math.degrees(radians)}°")

# ============================================================================
# 5. COMBINED EXAMPLES
# ============================================================================
print("\n" + "=" * 70)
print("5. COMBINED EXAMPLES")
print("=" * 70)

# Example 1: Create event reminders (Iterator + Date)
print("\n--- Example 1: Event Reminders (Iterator + Date) ---")
class EventReminder:
    def __init__(self, event_name, start_date, num_reminders):
        self.event_name = event_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.num_reminders = num_reminders
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.num_reminders:
            reminder_date = self.start_date - timedelta(days=(self.num_reminders - self.current))
            self.current += 1
            return f"Reminder for '{self.event_name}' on {reminder_date.date()}"
        raise StopIteration

reminders = EventReminder("Conference", "2026-06-15", 3)
print("Reminders:")
for reminder in reminders:
    print(f"  {reminder}")

# Example 2: Math calculations with date range
print("\n--- Example 2: Calculate Days-between Statistics ---")
from_date = datetime(2026, 1, 1)
to_date = datetime(2026, 12, 31)
days_in_year = (to_date - from_date).days

print(f"Total days in 2026: {days_in_year}")
print(f"Square root of days: {math.sqrt(days_in_year):.2f}")
print(f"Half the days: {days_in_year / 2:.0f}")
print(f"Average hours per day: {24}")

print("\n" + "=" * 70)
print("Demo Complete!")
print("=" * 70)
