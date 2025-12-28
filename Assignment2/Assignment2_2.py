"""
What is the difference between:
a = 10
b = 10

and 

a = [10]
b = [10]

explain using id function.
"""

a = 10
b = 10

print(id(a))   # op-> 140718927971528 
print(id(b))   # op-> 140718927971528

# Explanation -
# Same value in different variables have same memory address

a = [10]
b = [10]

print(id(a))   # op-> 1771336130624
print(id(b))   # op-> 1771336278976

# Explanation -
# list datatypes with same values or different values have the different memory address

"""
The core difference is object identity: the first case creates two references to a single shared integer object, while the second case creates two independent list objects, which is verifiable using the id() function which returns distinct identifiers for the lists.
"""