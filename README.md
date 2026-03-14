# Numpy-analysis

SAMPLE OUTPUT

=== TASK 1: Array Creation and Properties ===

Array 1 - Random Integers:
[23 45 12 ... 34 8 41]
Shape: (100,)
Dimensions: 1
Size: 100
Data Type: int64
Item Size: 8 bytes

Array 2 - Ones converted to int:
[[1 1 1 1 1 1]
 [1 1 1 1 1 1]
 ...
Shape: (5, 6)
Dimensions: 2
Size: 30
Data Type: int64
Item Size: 8 bytes

[Similar output for arrays 3 and 4]

=== TASK 2: Memory and Speed Comparison ===

Memory Consumption:
Python List: 87624 bytes
NumPy Array: 80000 bytes
Memory Saved: 7624 bytes

Speed Comparison:
List Addition Time: 0.0123 seconds
NumPy Addition Time: 0.0008 seconds
NumPy is 15.38x faster than Python lists

=== TASK 3: Sales Data Analysis ===

Sales Data Shape: (30, 4)

Total Sales by Product:
Product 1: 18450
Product 2: 19230
Product 3: 17890
Product 4: 20100

Average Daily Sales Across All Products:
[625.5 580.3 ... 710.8]

Day with Maximum Sales: Day 15 (Total: 3250)
Product with Minimum Average Sales: Product 3 (Average: 596.33)

Memory Optimization:
Original dtype: int64 (8 bytes per element)
New dtype: float32 (4 bytes per element)
Memory saved per element: 4 bytes
Total memory saved: 480 bytes (for 120 elements)
