"""
Write a program to take user's name and age and display:

Hello <name>, you will turn <age+1> next year.
"""

name = input("Enter your name : ")
age = int(input("Enter your Age : "))

print("Hello " + name + ", you will turn " + str(age + 1) + " next year.")
print()
print(f"Hello {name}, you will turn {age + 1} next yaer.")