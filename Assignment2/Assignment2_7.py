"""
Why does the input() function always return a string?
How can you convert it into another data type?
"""

# Answer 
"""
The input() function reads user input as text from the keyboard,
so it always returns a string to avoid data loss and allow flexible 
processing. 
"""

a = input("Enter a number : ")   # 10
print(type(a))                   # <class 'str'>

# We can convert it into another data type by using typecasting

a = int(a)                       # convert to integer
print(type(a))                   # <class 'int'>

# In Similar way we can do this with
# int(a)
# float(a)
