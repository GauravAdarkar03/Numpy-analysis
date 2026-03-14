import sys
import time
import numpy as np

print("=== TASK 1: Array Creation and Properties ===\n")

# Array 1: 1D array of 100 random integers between 1 and 50
arr1 = np.random.randint(1, 51, 100)

print("Array 1 - Random Integers:")
print(arr1)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)
print("Item Size:", arr1.itemsize, "bytes\n")


# Array 2: 2D array of ones (5x6) converted to int
arr2 = np.ones((5,6)).astype(int)

print("Array 2 - Ones converted to int:")
print(arr2)
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)
print("Item Size:", arr2.itemsize, "bytes\n")


# Array 3: 1D array of 20 evenly spaced values between 0 and 100
arr3 = np.linspace(0,100,20)

print("Array 3 - Evenly Spaced Values:")
print(arr3)
print("Shape:", arr3.shape)
print("Dimensions:", arr3.ndim)
print("Size:", arr3.size)
print("Data Type:", arr3.dtype)
print("Item Size:", arr3.itemsize, "bytes\n")


# Array 4: 3x3 identity matrix
arr4 = np.eye(3)

print("Array 4 - Identity Matrix:")
print(arr4)
print("Shape:", arr4.shape)
print("Dimensions:", arr4.ndim)
print("Size:", arr4.size)
print("Data Type:", arr4.dtype)
print("Item Size:", arr4.itemsize, "bytes\n")


print("=== TASK 2: Memory and Speed Comparison ===\n")

# Python list
py_list1 = list(range(1,10001))
py_list2 = list(range(1,10001))

# NumPy arrays
np_array1 = np.arange(1,10001)
np_array2 = np.arange(1,10001)

# Memory usage
list_memory = sys.getsizeof(py_list1)
numpy_memory = np_array1.nbytes

print("Memory Consumption:")
print("Python List:", list_memory, "bytes")
print("NumPy Array:", numpy_memory, "bytes")
print("Memory Saved:", list_memory - numpy_memory, "bytes\n")

# Speed comparison for list addition
start = time.time()
list_result = [a + b for a,b in zip(py_list1,py_list2)]
list_time = time.time() - start

# Speed comparison for NumPy addition
start = time.time()
numpy_result = np_array1 + np_array2
numpy_time = time.time() - start

print("Speed Comparison:")
print("List Addition Time:", list_time, "seconds")
print("NumPy Addition Time:", numpy_time, "seconds")

print("NumPy is", round(list_time/numpy_time,2), "x faster than Python lists\n")

print("=== TASK 3: Sales Data Analysis ===\n")

# Generate sales data
sales = np.random.randint(100,1001,(30,4))

print("Sales Data Shape:", sales.shape)
print("\nSales Data:\n", sales)

# Total sales per product
product_sales = sales.sum(axis=0)

print("\nTotal Sales by Product:")
for i,val in enumerate(product_sales):
    print(f"Product {i+1}: {val}")

# Average daily sales across products
daily_avg = sales.mean(axis=1)

print("\nAverage Daily Sales Across All Products:")
print(daily_avg)

# Day with maximum total sales
daily_total = sales.sum(axis=1)
max_day = np.argmax(daily_total)

print("\nDay with Maximum Sales: Day", max_day+1, "(Total:", daily_total[max_day], ")")

# Product with minimum average sales
product_avg = sales.mean(axis=0)
min_product = np.argmin(product_avg)

print("\nProduct with Minimum Average Sales: Product", min_product+1,
      "(Average:", round(product_avg[min_product],2), ")")

# Memory optimization
sales_float = sales.astype(np.float32)

print("\nMemory Optimization:")
print("Original dtype:", sales.dtype, "(", sales.itemsize, "bytes per element )")
print("New dtype:", sales_float.dtype, "(", sales_float.itemsize, "bytes per element )")

saved_per_element = sales.itemsize - sales_float.itemsize
total_elements = sales.size

print("Memory saved per element:", saved_per_element, "bytes")
print("Total memory saved:", saved_per_element * total_elements, "bytes")