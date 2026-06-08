import numpy as np

"""NumPy introduction demo.

This file shows common NumPy functionality:
- create arrays from lists
- inspect shape and dtype
- perform arithmetic and matrix operations
- slice, index, and boolean-filter arrays
- use NumPy math functions and statistics
"""

# Basic array creation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("arr1:")
print(arr1)
print("shape:", arr1.shape)
print("dtype:", arr1.dtype)
print()

print("arr2:")
print(arr2)
print("shape:", arr2.shape)
print("dtype:", arr2.dtype)
print()

# Create special arrays
zeros = np.zeros((2, 3))
identity = np.eye(3)
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("zeros:")
print(zeros)
print("identity:")
print(identity)
print("arange:", range_arr)
print("linspace:", linspace_arr)
print()

# Arithmetic operations
sum_arr = arr1 + 10
product_arr = arr1 * 2
square_arr = arr1 ** 2

print("arr1 + 10:", sum_arr)
print("arr1 * 2:", product_arr)
print("arr1 squared:", square_arr)
print()

# Matrix multiplication and transpose
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
mat_prod = mat_a @ mat_b
mat_transpose = mat_b.T

print("mat_a:")
print(mat_a)
print("mat_b:")
print(mat_b)
print("mat_a @ mat_b:")
print(mat_prod)
print("mat_b transpose:")
print(mat_transpose)
print()

# Indexing and slicing
print("arr2[0, 1]:", arr2[0, 1])
print("arr2 first row:", arr2[0])
print("arr2 first column:", arr2[:, 0])
print("arr2 submatrix:")
print(arr2[0:2, 1:3])
print()

# Boolean indexing
mask = arr1 % 2 == 0
even_numbers = arr1[mask]
print("even numbers from arr1:", even_numbers)
print()

# Math and statistics
print("sum of arr1:", np.sum(arr1))
print("mean of arr1:", np.mean(arr1))
print("standard deviation of arr1:", np.std(arr1))
print("sqrt of arr1:", np.sqrt(arr1))
print()

# Reshaping arrays
reshaped = np.arange(12).reshape(3, 4)
print("reshaped 3x4 array:")
print(reshaped)
print()

# Broadcasting example
small = np.array([1, 2, 3])
broadcasted = np.array([[10], [20], [30]]) + small
print("broadcasted addition result:")
print(broadcasted)
