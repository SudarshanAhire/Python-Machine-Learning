"""
Predict the output:
a = 10
b = 10
print(id(a) == id(b))

Explain why this happens.
"""

a = 10
b = 10

print(id(a) == id(b))  # True

#Answer
"""
In python small integers (usually from -5 to 256) are cached. Since 10 falls in this range, both a and b refer to the same memory object. Therefore id(a) and id(b) are equal.
And also the behavior of python due to its memory optimization technique.
"""

