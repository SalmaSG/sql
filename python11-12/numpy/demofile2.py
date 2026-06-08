import numpy as np

"""NumPy Data Types, Copy, Views, Reshape, and Iteration Demo.

This file demonstrates:
- NumPy data types (dtype)
- Array copy vs. views
- Array shape and reshaping
- Iterating over arrays
"""

print("=" * 60)
print("1. DATA TYPES (dtype)")
print("=" * 60)

# Different data types
int_arr = np.array([1, 2, 3, 4, 5])
float_arr = np.array([1.5, 2.5, 3.5])
bool_arr = np.array([True, False, True])
string_arr = np.array(['a', 'b', 'c'])
complex_arr = np.array([1+2j, 3+4j])

print(f"int_arr dtype: {int_arr.dtype}")
print(f"float_arr dtype: {float_arr.dtype}")
print(f"bool_arr dtype: {bool_arr.dtype}")
print(f"string_arr dtype: {string_arr.dtype}")
print(f"complex_arr dtype: {complex_arr.dtype}")
print()

# Specifying dtype explicitly
uint8_arr = np.array([1, 2, 3], dtype=np.uint8)
float32_arr = np.array([1.5, 2.5, 3.5], dtype=np.float32)
int64_arr = np.array([1, 2, 3], dtype=np.int64)

print(f"uint8_arr dtype: {uint8_arr.dtype}")
print(f"float32_arr dtype: {float32_arr.dtype}")
print(f"int64_arr dtype: {int64_arr.dtype}")
print()

# Converting between data types
converted = int_arr.astype(float)
print(f"Original int_arr: {int_arr}, dtype: {int_arr.dtype}")
print(f"Converted to float: {converted}, dtype: {converted.dtype}")
print()

print("=" * 60)
print("2. COPY vs. VIEWS")
print("=" * 60)

original_arr = np.array([10, 20, 30, 40, 50])
print(f"Original array: {original_arr}")
print()

# VIEW: Does not copy data, just references original
view_arr = original_arr[1:4]
print(f"View (slice): {view_arr}")
print(f"View shares data: {view_arr.base is original_arr}")

# Modifying view affects original
view_arr[0] = 999
print(f"After modifying view[0] = 999:")
print(f"  Original array: {original_arr}")
print(f"  View: {view_arr}")
print()

# Reset for next demo
original_arr = np.array([10, 20, 30, 40, 50])

# COPY: Creates independent copy of data
copy_arr = original_arr[1:4].copy()
print(f"Copy: {copy_arr}")
print(f"Copy is independent: {copy_arr.base is original_arr}")

# Modifying copy does NOT affect original
copy_arr[0] = 888
print(f"After modifying copy[0] = 888:")
print(f"  Original array: {original_arr}")
print(f"  Copy: {copy_arr}")
print()

# Using .copy() method explicitly
explicit_copy = original_arr.copy()
explicit_copy[2] = 777
print(f"After modifying explicit_copy[2] = 777:")
print(f"  Original array: {original_arr}")
print(f"  Explicit copy: {explicit_copy}")
print()

print("=" * 60)
print("3. ARRAY SHAPE AND RESHAPE")
print("=" * 60)

# Understanding shape
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(f"1D array: {arr_1d}")
print(f"Shape: {arr_1d.shape}, Size: {arr_1d.size}")
print()

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}, Size: {arr_2d.size}")
print()

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3D array:\n{arr_3d}")
print(f"Shape: {arr_3d.shape}, Size: {arr_3d.size}")
print()

# Reshaping arrays (reshape returns a view, not a copy)
print("RESHAPING:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Original shape: {arr.shape}, array: {arr}")

reshaped_2d = arr.reshape(3, 4)
print(f"Reshape to (3, 4):\n{reshaped_2d}")

reshaped_3d = arr.reshape(2, 3, 2)
print(f"Reshape to (2, 3, 2):\n{reshaped_3d}")

reshaped_back = reshaped_2d.reshape(12)
print(f"Reshape back to (12,): {reshaped_back}")
print()

# Flatten and ravel (different approaches)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original 2D array:\n{arr_2d}")

flattened = arr_2d.flatten()  # Returns a copy
print(f"Flattened (copy): {flattened}")

raveled = arr_2d.ravel()  # Returns a view
print(f"Raveled (view): {raveled}")

# Modifying raveled affects original
raveled[0] = 999
print(f"After modifying raveled[0] = 999:")
print(f"  Original: \n{arr_2d}")
print()

# Transpose
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
transposed = arr_2d.T
print(f"Original:\n{arr_2d}")
print(f"Transposed:\n{transposed}")
print()

print("=" * 60)
print("4. ITERATING OVER ARRAYS")
print("=" * 60)

# Iterating over 1D array
arr_1d = np.array([10, 20, 30, 40])
print("Iterating over 1D array:")
for element in arr_1d:
    print(f"  Element: {element}")
print()

# Iterating over 2D array (iterates over rows)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Iterating over 2D array (iterates over rows):")
for row in arr_2d:
    print(f"  Row: {row}")
print()

# Using flat for flattened iteration
print("Iterating using .flat (flattened):")
for element in arr_2d.flat:
    print(f"  Element: {element}")
print()

# Using nditer for more control
print("Iterating using np.nditer (with options):")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
for element in np.nditer(arr_2d):
    print(f"  Element: {element}")
print()

# Using ndenumerate for index and value
print("Iterating using np.ndenumerate (with indices):")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
for index, element in np.ndenumerate(arr_2d):
    print(f"  Index {index}: {element}")
print()

# Iterating over 3D array
print("Iterating over 3D array (iterates over 2D matrices):")
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for matrix in arr_3d:
    print(f"  Matrix:\n{matrix}")
print()

# Using enumerate with 1D array
print("Using enumerate with 1D array:")
arr = np.array([100, 200, 300, 400])
for i, value in enumerate(arr):
    print(f"  Index {i}: {value}")
print()

print("=" * 60)
print("5. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Data type conversion for memory efficiency
print("Example 1: Memory efficient data storage")
large_list = list(range(1000000))
arr_int64 = np.array(large_list, dtype=np.int64)
arr_int32 = np.array(large_list, dtype=np.int32)
arr_int8 = np.array(large_list[:256], dtype=np.int8)  # Only first 256 elements fit

print(f"Int64 size: {arr_int64.nbytes} bytes")
print(f"Int32 size: {arr_int32.nbytes} bytes")
print(f"Int8 size (256 elements): {arr_int8.nbytes} bytes")
print()

# Example 2: Safe modifications using copy
print("Example 2: Safe data manipulation with copy")
original_data = np.array([1, 2, 3, 4, 5])
working_copy = original_data.copy()
working_copy = working_copy * 2 + 10
print(f"Original: {original_data}")
print(f"Modified copy: {working_copy}")
print()

# Example 3: Reshaping for matrix operations
print("Example 3: Reshaping for operations")
scores = np.array([85, 90, 78, 92, 88, 95, 81, 87, 91, 86])
print(f"Flat scores: {scores}")
scores_matrix = scores.reshape(5, 2)
print(f"Reshaped as (5 students, 2 tests):\n{scores_matrix}")
print(f"Average per student: {scores_matrix.mean(axis=1)}")
print()

# Example 4: Efficient batch processing with iteration
print("Example 4: Batch processing with iteration")
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Processing each row:")
for i, row in enumerate(data):
    print(f"  Row {i}: sum={row.sum()}, mean={row.mean():.2f}")
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Points:
1. dtype: Specifies the data type of array elements
   - Use appropriate dtype for memory efficiency
   - Convert between types using astype()

2. Copy vs. Views:
   - Views share data with original (slicing, reshape)
   - Copies are independent (copy(), flatten())
   - Modifying a view affects the original

3. Shape and Reshape:
   - shape: tuple describing array dimensions
   - reshape(): changes dimensions without changing data
   - flatten(): creates a copy; ravel(): creates a view

4. Iteration:
   - Simple loop: iterates over first dimension
   - .flat: flattens for element-by-element iteration
   - np.nditer(): advanced iteration control
   - np.ndenumerate(): iteration with indices
""")
