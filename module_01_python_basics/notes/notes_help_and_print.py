# ============================================================
# Python Basics Notes: help(), round(), and print()
# ============================================================


# 1. THE help() FUNCTION
# ------------------------------------------------------------
# The help() function displays documentation about a function.
#
# Example:
# help(round)
#
# Here, round refers to the function itself. We are asking
# Python to explain how the function works.


# 2. FUNCTION ITSELF vs. FUNCTION CALL
# ------------------------------------------------------------
# help(round) asks for documentation about the round function.
#
# help(round(-2.01)) first evaluates round(-2.01), which
# returns -2. Then help() displays documentation about the
# resulting integer object, not the round function itself.
#
# Remember:
#   round     -> the function itself
#   round()   -> calling the function


# 3. THE round() FUNCTION
# ------------------------------------------------------------
# Function header:
# round(number, ndigits=None)
#
# number  : the number we want to round
# ndigits : optional argument specifying decimal precision
#
# Example A: Round to the nearest integer
print(round(3.7))          # Output: 4

# Example B: Round to two decimal places
print(round(3.14159, 2))   # Output: 3.14

# Example C: Omit the optional argument
print(round(3.14159))      # Output: 3


# 4. THE print() FUNCTION
# ------------------------------------------------------------
# help(print) displays documentation about print().
#
# Simplified function header:
# print(value, ..., sep=' ', end='\n', file=..., flush=False)
#
# sep   : separator between multiple values
# end   : what to print after the output
# file  : where the output is sent
# flush : whether to force the output buffer to flush
#
# For now, focus on sep and end.


# 5. USING sep
# ------------------------------------------------------------
# By default, sep=" " (a space).
# It controls what appears BETWEEN multiple values.

print("Hello", "World")
# Output: Hello World

print("Hello", "World", sep="-")
# Output: Hello-World

print("Hello", "World", sep="***")
# Output: Hello***World

print("A", "B", "C", sep="")
# Output: ABC


# 6. USING end
# ------------------------------------------------------------
# By default, end="\n" (a newline).
# It controls what appears AFTER the printed values.
#
# Normally, each print() call starts a new line.

print("Hello", "World")
print("Python", "is fun")

# Output:
# Hello World
# Python is fun


# We can change end to a space instead of a newline.

print("Hello", end=" ")
print("World")

# Output:
# Hello World


# We can also use another string as the ending.

print("Hello", end="***")
print("World")

# Output:
# Hello***World


# ============================================================
# KEY TAKEAWAYS
# ============================================================
# 1. help(function_name) displays documentation about a function.
# 2. round(number) rounds a number to the nearest integer.
# 3. round(number, ndigits) rounds to the specified precision.
# 4. sep controls the separator BETWEEN printed values.
# 5. end controls what appears AFTER the printed output.
# ============================================================