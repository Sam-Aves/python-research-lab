
# ============================================================
# TASK 10: FUNCTIONS AND ARGUMENTS
# Module 01 - Python Basics
# ============================================================

# Topics:
# - Defining and calling functions
# - Parameters and arguments
# - Return values and None
# - Docstrings
# - Default arguments
# - Higher-order functions
# - max() with a key function


# ------------------------------------------------------------
# TASK 1: BASIC FUNCTION
# ------------------------------------------------------------

# Define a function called calculate_discounted_price().
# It should accept price and discount_percent.
#
# Calculate the discount amount and return the final price.
#
# Example:
# calculate_discounted_price(1000, 20) -> 800.0
# calculate_discounted_price(500, 10) -> 450.0
#
# Assume discount_percent is given as a percentage from
# 0 to 100.

def calculate_discounted_price(price, discount_percent):
    """
    calculates the discount price of a product
    Args: 
    price- price of the product
    discount_percent- percentage of discount
    calculate_discounted_price(1000,25)
    >>> 750.0
    """
    discount_amount = price * (discount_percent / 100)
    discounted_price = price - discount_amount
    return discounted_price


print(calculate_discounted_price(1000, 20))
print(calculate_discounted_price(500, 10))


# ------------------------------------------------------------
# TASK 2: DOCSTRING AND HELP
# ------------------------------------------------------------

# Add a useful docstring to calculate_discounted_price().
#
# Your docstring should explain:
# - What the function does.
# - What each parameter represents.
# - What the function returns.
#
# Then inspect the function using help().
help(calculate_discounted_price)


# ------------------------------------------------------------
# TASK 3: RETURN VS PRINT
# ------------------------------------------------------------

# Define a function called display_difference(a, b).
# It should print the absolute difference between a and b.
#
# Call the function and assign its result to a variable.
# Print that variable.
#
# Observe the difference between the displayed difference
# and the value stored in the variable.

def display_difference(a, b):
    diff = abs(a-b)
    return diff


diff = display_difference(15, 8)
print(diff)

# ------------------------------------------------------------
# TASK 4: DEFAULT ARGUMENTS
# ------------------------------------------------------------

# Define a function called introduce_student().
#
# Parameters:
# - name, default value "Student"
# - department, default value "CSE"
#
# The function should print a sentence introducing the
# student and their department.
#
# Test all three cases:
# 1. Call without arguments.
# 2. Call with only a name.
# 3. Call with both arguments using keyword arguments.

def introduce_student(name="Student", department="CSE"):
    print(f"My name is {name} and I am a student of {department} department.")


# TODO: Write the three function calls here.

introduce_student()
introduce_student("Bob")
introduce_student("Alice", "CCE")


# ------------------------------------------------------------
# TASK 5: HIGHER-ORDER FUNCTION
# ------------------------------------------------------------

# Define a function called apply_twice(fn, value).
#
# It should apply the supplied function to value twice
# in succession and return the final result.
#
# Define another function called add_three(x), which returns
# x + 3.
#
# Expected result:
# apply_twice(add_three, 4) -> 10
#
# Trace the two function calls to understand the result.

def apply_twice(fn, value):
    fn(value)
    fn(value)


def add_three(x):
   return 3 * x


# TODO: Print apply_twice(add_three, 4).
print(apply_twice(add_three, 4))

# ------------------------------------------------------------
# TASK 6: FIND THE NUMBER WITH THE LARGEST REMAINDER
# ------------------------------------------------------------

# Define a function called remainder_by_seven(x).
# It should return the remainder when x is divided by 7.
#
# Use max() with key=remainder_by_seven to find the number
# with the largest remainder from this list:
#
# numbers = [22, 31, 18, 45, 26]
#
# Do not sort the list or manually choose the answer.
# Use the key argument to max().

def remainder_by_seven(x):
    return x % 7


numbers = [22, 31, 18, 45, 26]

print(max(numbers, key=remainder_by_seven))
print(max(numbers))

# ------------------------------------------------------------
# TASK 7: FIND THE LONGEST NAME
# ------------------------------------------------------------

# Given a list of student names, find the longest name using
# max() and len as the key function.
#
# Do not calculate the lengths manually.

student_names = [
    "Amina",
    "Christopher",
    "Nadia",
    "Mahmudul"
]

# TODO: Find and print the longest name using max().
print(max(student_names, key=len))

