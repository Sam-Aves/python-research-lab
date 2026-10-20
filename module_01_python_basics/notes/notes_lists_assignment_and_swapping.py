
# ==========================================
# LISTS, ASSIGNMENT, AND SWAPPING VARIABLES
# ==========================================

# A list stores multiple items in one variable.
# Lists are written using square brackets [].

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Lists can contain different data types.
items = ["Python", 10, 3.5, True]
print(items)

# Access list elements using indexes.
# Python indexing starts at 0.

print(numbers[0])    # First item: 1
print(numbers[1])    # Second item: 2
print(numbers[-1])   # Last item: 5

# Lists are mutable: their contents can be changed.
numbers[0] = 100
print(numbers)

# ------------------------------------------
# ASSIGNMENT AND REFERENCES
# ------------------------------------------

a = [1, 2, 3]
b = a

# b = a does not create an independent copy.
# Both names refer to the same list object.

b[0] = 99
print(a)             # [99, 2, 3]
print(b)             # [99, 2, 3]

# If you need a shallow copy of a list:
a = [1, 2, 3]
b = a.copy()

b[0] = 99
print(a)             # [1, 2, 3]
print(b)             # [99, 2, 3]

# ------------------------------------------
# SWAPPING TWO VARIABLES
# ------------------------------------------

# Method 1: Use a temporary variable.

a = 10
b = 20

temp = a
a = b
b = temp

print(a)             # 20
print(b)             # 10

# Why does this work?
# 1. Save the original value of a in temp.
# 2. Put b's value into a.
# 3. Put the saved value into b.

# Method 2: Python supports tuple unpacking.
# This is a common Python way to swap variables.

a = 10
b = 20

a, b = b, a

print(a)             # 20
print(b)             # 10

# Task 6 used lists rather than simple numbers.
# The same swapping pattern works for both.
# Remember that assigning a list to another variable
# does not automatically copy the list.
