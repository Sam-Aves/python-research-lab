
# ==========================================
# VARIABLES AND DATA TYPES
# ==========================================

# A variable is a name that refers to a value.
# The = operator assigns a value to a variable.

name = "Alice"             # str: text
age = 23                   # int: integer
cgpa = 3.998               # float: decimal number
is_student = True          # bool: True or False

# Python is dynamically typed.
# We do not need to declare a variable's type in advance.

print(name)
print(type(name))          # type() tells us the data type
print(type(age))
print(type(cgpa))
print(type(is_student))

# Variable names are case-sensitive.
score = 90
Score = 95                 # Different variable from score

# Naming rules:
# 1. Names can contain letters, numbers, and underscores.
# 2. Names cannot start with a number.
# 3. Names cannot contain spaces.
# 4. Use descriptive names for readability.

completed_credits = 100
temperature_celsius = 25.5

# Variables can be reassigned.
score = 90
score = 95

# Multiple assignment
x, y = 10, 20

# Constants are usually written in uppercase by convention.
PI = 3.1416

# Lists store multiple values in one variable.
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

# Remember:
# =  means assignment
# == means comparison for equality
