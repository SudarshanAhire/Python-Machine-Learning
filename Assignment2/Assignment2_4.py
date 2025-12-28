"""
What is the purpose of getsizeof()?
Why is memory size different for different data types?
"""

from sys import getsizeof 

a = 10
b = 3.14
c = "Marvellous"

print(getsizeof(a))   # op-> 28
print(getsizeof(b))   # op-> 24
print(getsizeof(c))   # op-> 51

# Answer
"""
The getsizeof() function returns the memory size (in bytes) occupied by an object.
The purpose of getsizeof() function is to understand memory usage, differece between data types and performance optimization.
Memory size is different for different data types because each data type is designed to store a specific kind and range of values, and the computer allocates only as much memory as needed to represent those values efficiently.
"""