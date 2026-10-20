
# ============================================================
# NOTES: FUNCTIONS, HELP, DOCSTRINGS, AND HIGHER-ORDER FUNCTIONS
# Module 01 - Python Basics
# Source: Kaggle Python Course - Functions
# ============================================================


# ------------------------------------------------------------
# 1. GETTING HELP WITH BUILT-IN FUNCTIONS
# ------------------------------------------------------------

# Python provides built-in functions such as print(), abs(),
# round(), min(), max(), and len().
#
# The help() function displays information about a function,
# including its signature and documentation.

# help(round)
# help(print)
# help(abs)

# IMPORTANT:
# Pass the function itself to help(), not a function call.
#
# Correct:
# help(round)
#
# Incorrect for looking up round's documentation:
# help(round(-2.01))
#
# In the incorrect example, Python first evaluates round(-2.01)
# and then tries to display help for the resulting number.

# Function signature:
# round(number, ndigits=None)
#
# number: The number to round.
# ndigits: Optional argument specifying decimal precision.
# None: The default value when ndigits is omitted.


# ------------------------------------------------------------
# 2. DEFINING YOUR OWN FUNCTIONS
# ------------------------------------------------------------

# Use the def keyword to define a function.
#
# Syntax:
#
# def function_name(parameters):
#     statements
#     return value
#
# A function definition does not execute its body immediately.
# The body runs when the function is called.

def calculate_square(number):
    return number * number


# Calling the function:
print(calculate_square(5))  # Output: 25

# Here:
# calculate_square = function name
# number = parameter
# 5 = argument supplied during the call
# number * number = expression being evaluated
# return = sends the result back to the caller


# ------------------------------------------------------------
# 3. PARAMETERS AND ARGUMENTS
# ------------------------------------------------------------

# A parameter is a variable named in the function definition.
# An argument is the actual value supplied when calling it.

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


# Positional arguments: values are matched by their positions.
introduce("Sam", 23)

# Keyword arguments: values are matched by parameter names.
introduce(age=23, name="Sam")

# Keyword arguments allow us to supply arguments in a different
# order because their parameter names are explicitly specified.


# ------------------------------------------------------------
# 4. RETURN STATEMENTS
# ------------------------------------------------------------

# The return statement:
# 1. Ends the function immediately.
# 2. Sends a value back to the calling code.
#
# The returned value can be stored, printed, or used in
# another calculation.

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print(result)                  # Output: 30
print(add_numbers(5, 3) * 2)  # Output: 16


# RETURN VS PRINT:
#
# print() displays a value on the screen.
# return sends a value back to the caller.
#
# These operations are NOT interchangeable.

def show_sum(a, b):
    print(a + b)


def get_sum(a, b):
    return a + b


shown = show_sum(2, 3)  # Displays 5
print(shown)            # Displays None

returned = get_sum(2, 3)
print(returned)         # Displays 5


# ------------------------------------------------------------
# 5. FUNCTIONS WITHOUT A RETURN STATEMENT
# ------------------------------------------------------------

# If a function finishes without executing a return statement,
# Python automatically returns None.
#
# None is a special Python value representing the absence of
# a returned value.

def display_message():
    print("Learning Python functions!")


output = display_message()
# The function displays a message.
print(output)  # Output: None


# Some functions are useful because of their side effects.
# Examples include displaying text or writing to a file.
#
# A side effect is an action performed by a function beyond
# simply calculating and returning a value.


# ------------------------------------------------------------
# 6. ABSOLUTE DIFFERENCE AND THE LEAST DIFFERENCE EXAMPLE
# ------------------------------------------------------------

# abs() returns the absolute value of a number.
# An absolute value is never negative.

print(abs(-10))  # Output: 10
print(abs(10))   # Output: 10

# min() returns the smallest value among its arguments.

print(min(8, 3, 5))  # Output: 3


def least_difference(a, b, c):
    """Return the smallest absolute difference among three numbers.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

    return min(diff1, diff2, diff3)


print(least_difference(1, 5, -5))  # Output: 4
print(least_difference(10, 40, 90))  # Output: 30

# The function calculates all three pairwise differences.
# It then returns the smallest one.
#
# For three values a, b, and c:
# diff1 = |a - b|
# diff2 = |b - c|
# diff3 = |a - c|


# ------------------------------------------------------------
# 7. DOCSTRINGS
# ------------------------------------------------------------

# A docstring is a string that documents a function, class,
# or module.
#
# A function's docstring must appear immediately after its
# definition header, before other statements in its body.
#
# Triple double quotes are commonly used for docstrings.

def calculate_area(length, width):
    """Return the area of a rectangle.

    Args:
        length: The rectangle's length.
        width: The rectangle's width.

    Returns:
        The area calculated by multiplying length and width.
    """
    return length * width


print(calculate_area(5, 4))  # Output: 20

# help() displays the function's documentation.
# Uncomment the next line to inspect it.
# help(calculate_area)

# A docstring explains what a function does, what its inputs
# mean, and what it returns.
#
# >>> examples inside a docstring are illustrative examples.
# They are not automatically executed simply because they
# appear inside the docstring.


# ------------------------------------------------------------
# 8. DEFAULT ARGUMENTS
# ------------------------------------------------------------

# A default argument value is used when the caller omits
# that argument.

def greet(who="Colin"):
    print("Hello,", who)


greet()                   # Output: Hello, Colin
greet("Sam")              # Output: Hello, Sam
greet(who="Kaggle")       # Output: Hello, Kaggle

# Positional argument:
# greet("Sam")
#
# Keyword argument:
# greet(who="Sam")
#
# Both calls produce the same result here.
#
# Default values make arguments optional for the caller.

# Built-in functions also have optional arguments.
#
# print(1, 2, 3)
# Output: 1 2 3
#
# print(1, 2, 3, sep=" < ")
# Output: 1 < 2 < 3
#
# sep defaults to a single space.
# end defaults to a newline character ("\n").


# ------------------------------------------------------------
# 9. PASSING FUNCTIONS AS ARGUMENTS
# ------------------------------------------------------------

# Python allows functions to be passed as arguments to other
# functions. Functions can be treated as values.
#
# IMPORTANT DISTINCTION:
#
# mult_by_five  -> refers to the function itself
# mult_by_five(2) -> calls the function and produces a result

def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call the supplied function once on the argument."""
    return fn(arg)


print(call(mult_by_five, 2))  # Output: 10

# How it works:
# fn = mult_by_five
# arg = 2
# fn(arg) is equivalent to mult_by_five(2).
#
# The outer function calls the function it receives.


# ------------------------------------------------------------
# 10. HIGHER-ORDER FUNCTIONS
# ------------------------------------------------------------

# A higher-order function accepts another function as an
# argument or returns a function.
#
# call() is a higher-order function because it accepts fn.

def add_ten(x):
    return x + 10


print(call(add_ten, 5))  # Output: 15

# The same call() function works with different functions.
# Its behavior depends on which function is supplied.

# A function can call another function more than once.

def squared_call(fn, arg):
    """Call fn twice in succession on the argument."""
    return fn(fn(arg))


print(squared_call(mult_by_five, 1))  # Output: 25

# Execution:
# fn(1)       -> 5
# fn(5)       -> 25
#
# squared_call does NOT necessarily square a number.
# It applies the supplied function twice.


# ------------------------------------------------------------
# 11. USING max() WITH A KEY FUNCTION
# ------------------------------------------------------------

# Normally, max() returns the largest value.

print(max(100, 51, 14))  # Output: 100

# The optional key argument tells max() how to compare
# the candidate values.

def mod_5(x):
    """Return the remainder after dividing x by 5."""
    return x % 5


print(mod_5(100))  # Output: 0
print(mod_5(51))   # Output: 1
print(mod_5(14))   # Output: 4

print(max(100, 51, 14, key=mod_5))  # Output: 14

# Why does max() return 14?
#
# Original number    Remainder after division by 5
# 100                0
# 51                 1
# 14                 4
#
# The largest remainder is 4, which belongs to 14.
# max() returns the ORIGINAL value, not the remainder.
#
# key=mod_5 passes the function to max().
# It does not immediately call mod_5 on a single value.


# ------------------------------------------------------------
# 12. PRACTICAL EXAMPLE: FINDING THE LONGEST WORD
# ------------------------------------------------------------

# len() returns the length of a string.
# max() can use len as its key function.

words = ["cat", "elephant", "dog", "tiger"]

print(max(words, key=len))  # Output: elephant

# max() compares the lengths of the words:
# cat      -> 3
# elephant -> 8
# dog      -> 3
# tiger    -> 5
#
# It returns the original word with the greatest length.
#
# Other possible uses:
# - Find the student with the highest score.
# - Find the longest string.
# - Find the product with the highest price.
# - Select the value with the smallest calculated distance.

# ------------------------------------------------------------
# ROUNDING NUMBERS WITH round()
# ------------------------------------------------------------

# round(number, ndigits) rounds a number to a specified
# number of decimal places or to a power of 10.
#
# Positive ndigits: rounds to decimal places.
# Zero ndigits: rounds to the nearest integer.
# Negative ndigits: rounds to tens, hundreds, thousands, etc.

print(round(3.14159, 2))  # Output: 3.14
print(round(347, -1))     # Output: 350 (nearest 10)
print(round(347, -2))     # Output: 300 (nearest 100)
print(round(12345, -3))  # Output: 12000 (nearest 1000)

# Example: Simplifying large numbers
finland_area = 338424
greenland_area = 2166086

print(round(finland_area, -3))   # Output: 338000
print(round(greenland_area, -3))  # Output: 2166000

# Rounding can make large numbers easier to read when exact
# precision is unnecessary.
#
# IMPORTANT:
# round() rounds to the nearest value; it does not simply
# remove digits. Python also uses "ties to even" for exact
# halfway cases, such as round(2.5) -> 2 and round(3.5) -> 4.


# ------------------------------------------------------------
# 13. KEY TAKEAWAYS
# ------------------------------------------------------------

# 1. def defines a function.
# 2. Parameters are names in the function definition.
# 3. Arguments are values supplied during a function call.
# 4. return sends a value back and ends the function.
# 5. Functions without a returned value produce None.
# 6. Docstrings document functions and appear after the header.
# 7. help(function_name) displays documentation.
# 8. Default arguments provide fallback values.
# 9. Functions can be passed to other functions.
# 10. Higher-order functions accept or return functions.
# 11. max(..., key=function) compares values using a key.
# 12. print() displays values; it does not return those
#     displayed values.
