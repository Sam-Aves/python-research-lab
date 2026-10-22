
# ============================================================
# PYTHON NOTES: LOOPS AND LIST COMPREHENSIONS
# Module 01 - Python Basics
# ============================================================


# ------------------------------------------------------------
# 1. FOR LOOPS
# ------------------------------------------------------------

# A loop repeats a block of code.
# A for loop visits each item in an iterable, one at a time.

planets = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for planet in planets:
    print(planet)

# How it works:
# 1. Python takes the first item from planets.
# 2. It assigns that item to planet.
# 3. It executes the indented code.
# 4. It repeats for each remaining item.

# The loop variable can have any valid variable name.
for item in planets:
    print(item)

# Print all items on one line.
for planet in planets:
    print(planet, end=" ")


# ------------------------------------------------------------
# 2. LOOPS WITH TUPLES AND STRINGS
# ------------------------------------------------------------

# A for loop works with other iterables, not just lists.

multiplicands = (2, 2, 2, 3, 3, 5)

product = 1

for mult in multiplicands:
    product = product * mult

print("\nProduct:", product)  # 360

# A string is iterable, too.
# This loop visits each character individually.

message = "Python"

for char in message:
    print(char)

# Strings have useful methods such as isupper().
# isupper() returns True if a character is uppercase.

text = "Hello WORLD"

for char in text:
    if char.isupper():
        print(char, end="")

print()


# ------------------------------------------------------------
# 3. RANGE()
# ------------------------------------------------------------

# range() generates a sequence of integers.
# It is commonly used when you want to repeat something
# a specific number of times.

for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
# range(5) starts at 0 and stops before 5.

# range(start, stop)
for i in range(2, 6):
    print(i, end=" ")

# Output: 2 3 4 5

print()

# range(start, stop, step)
for i in range(2, 11, 2):
    print(i, end=" ")

# Output: 2 4 6 8 10

print()

# A negative step counts backward.
for i in range(5, 0, -1):
    print(i, end=" ")

# Output: 5 4 3 2 1

print()

# range() produces numbers; it does not include the stop value.


# ------------------------------------------------------------
# 4. WHILE LOOPS
# ------------------------------------------------------------

# A while loop repeats as long as its condition is True.

i = 0

while i < 5:
    print(i)
    i += 1

# i += 1 is shorthand for i = i + 1.
# Updating i eventually makes the condition False.
# Without an appropriate update, a loop might never end.

# Example: Count down.
countdown = 3

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Go!")


# ------------------------------------------------------------
# 5. FOR LOOP VS WHILE LOOP
# ------------------------------------------------------------

# Use a for loop when iterating over a sequence or range.
# Use a while loop when repetition depends on a condition.

# FOR LOOP:
for number in range(3):
    print("For:", number)

# WHILE LOOP:
number = 0

while number < 3:
    print("While:", number)
    number += 1


# ------------------------------------------------------------
# 6. LIST COMPREHENSIONS
# ------------------------------------------------------------

# A list comprehension creates a new list from an iterable.
#
# General structure:
# [expression for item in iterable]

# Example: Squares of numbers from 0 through 9.
squares = [n ** 2 for n in range(10)]

print(squares)

# Equivalent code using a regular for loop:
squares = []

for n in range(10):
    squares.append(n ** 2)

print(squares)

# Both approaches produce the same list.
# The comprehension is shorter when the transformation is simple.


# ------------------------------------------------------------
# 7. FILTERING WITH IF
# ------------------------------------------------------------

# A list comprehension can include a condition.
#
# General structure:
# [expression for item in iterable if condition]
#
# Only items satisfying the condition are included.

planets = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

short_planets = [
    planet for planet in planets if len(planet) < 6
]

print(short_planets)
# ['Venus', 'Earth', 'Mars']

# Read this as:
# Take each planet from planets,
# keep it only if its length is less than 6,
# and put it in the new list.


# ------------------------------------------------------------
# 8. FILTERING AND TRANSFORMING
# ------------------------------------------------------------

# The expression can transform each item that passes the filter.

loud_short_planets = [
    planet.upper() + "!"
    for planet in planets
    if len(planet) < 6
]

print(loud_short_planets)
# ['VENUS!', 'EARTH!', 'MARS!']

# Important:
# The expression comes before the for.
# The if at the end filters which items are included.


# ------------------------------------------------------------
# 9. THE EXPRESSION DOES NOT HAVE TO USE THE ITEM
# ------------------------------------------------------------

# This creates one 32 for every item in planets.

repeated_values = [32 for planet in planets]

print(repeated_values)

# There are 8 planets in the list, so there are 8 values.
# The loop variable controls how many times the expression runs.
# The expression itself does not have to use that variable.


# ------------------------------------------------------------
# 10. COUNTING NEGATIVE NUMBERS
# ------------------------------------------------------------

numbers = [5, -1, -2, 0, 3, -7]

# Method 1: Use a regular loop.

def count_negatives_loop(nums):
    """Return the number of negative values in nums."""

    count = 0

    for num in nums:
        if num < 0:
            count += 1

    return count


print(count_negatives_loop(numbers))  # 3


# Method 2: Use a list comprehension and len().

def count_negatives_comprehension(nums):
    """Count negative values using a list comprehension."""

    return len([num for num in nums if num < 0])


print(count_negatives_comprehension(numbers))  # 3

# The comprehension creates a list containing only negatives.
# len() counts how many items are in that list.


# ------------------------------------------------------------
# 11. COUNTING WITH BOOLEAN VALUES
# ------------------------------------------------------------

# Comparisons such as num < 0 return True or False.
# In Python, True behaves like 1 and False behaves like 0
# in arithmetic operations.

print(True + True + False)  # 2

# Therefore, we can sum the results of comparisons.

def count_negatives_sum(nums):
    """Count negative values by summing Boolean results."""

    return sum(num < 0 for num in nums)


print(count_negatives_sum(numbers))  # 3

# This version avoids building a separate list.
# It is compact, but the regular loop may be easier to
# understand when you're first learning.


# ------------------------------------------------------------
# 12. READABILITY MATTERS
# ------------------------------------------------------------

# List comprehensions are useful for simple transformations
# and filtering.

squares = [n ** 2 for n in range(10)]

# For more complicated logic, a regular loop can be clearer.
squares = []

for n in range(10):
    square = n ** 2
    squares.append(square)

# Both are valid.
# Prefer code that is easy to read and maintain.


# ------------------------------------------------------------
# KEY TAKEAWAYS
# ------------------------------------------------------------

# for loop:
# Repeats for each item in an iterable.

# range(stop):
# Generates integers starting at 0, stopping before stop.

# while loop:
# Repeats while its condition is True.

# List comprehension:
# [expression for item in iterable]

# Filtering:
# [expression for item in iterable if condition]

# len():
# Returns the number of items.

# sum():
# Adds numeric values, including Boolean results.

# Remember:
# Readability counts. Shorter code is not always clearer.


# ------------------------------------------------------------
# END OF NOTES
# ------------------------------------------------------------
