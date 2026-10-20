
# ==========================================
# CONDITIONAL STATEMENTS AND COMPARISONS
# ==========================================

# A conditional lets a program make decisions.
# Python uses if, elif, and else.

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# IMPORTANT: indentation defines the block of code.
# Use consistent indentation (normally 4 spaces).

# ------------------------------------------
# COMPARISON OPERATORS
# ------------------------------------------

a = 10
b = 5

print(a == b)    # False: equal to
print(a != b)    # True: not equal to
print(a > b)     # True: greater than
print(a < b)     # False: less than
print(a >= b)    # True: greater than or equal to
print(a <= b)    # False: less than or equal to

# A comparison evaluates to True or False.

# ------------------------------------------
# IF / ELIF / ELSE
# ------------------------------------------

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Keep practising.")

# Python checks conditions from top to bottom.
# The first matching branch is executed.

# ------------------------------------------
# PREVENTING DIVISION BY ZERO
# ------------------------------------------

numerator = 10
denominator = 2

if denominator != 0:
    print(numerator / denominator)
    print(numerator // denominator)
    print(numerator % denominator)
else:
    print("Division and modulo by zero are not allowed.")

# The != operator means "not equal to".
# This condition checks that the denominator is not zero.

# IMPORTANT:
# Checking before calculating prevents ZeroDivisionError.
# This is useful for /, //, and %.

# ------------------------------------------
# LOGICAL OPERATORS
# ------------------------------------------

# and: both conditions must be True
# or: at least one condition must be True
# not: reverses a Boolean value

age = 23
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

# These operators are useful when a decision depends
# on more than one condition.
