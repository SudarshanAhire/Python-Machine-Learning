"""
What does the id() function return?
Is the value returned by id() same for two variables holding the same value?
"""

a = 10
b = 10

print(id(a))  # op-> 140719346681032
print(id(b))  # op-> 140719346681032

# Answer
"""
id() function returns the memory address of the variable.
And the value returned by id() function is same for two different variables holding the same value. 
"""
