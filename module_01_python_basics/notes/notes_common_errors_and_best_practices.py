
# ==========================================
# COMMON ERRORS AND BEST PRACTICES
# ==========================================

# 1. INPUT RETURNS A STRING
# Incorrect for numerical calculation:
# age = input("Enter age: ")
# next_age = age + 1
#
# Correct:
age = int(input("Enter age: "))
next_age = age + 1
print(next_age)

# 2. INVALID TYPE CONVERSION
# int("hello") raises ValueError.
# float("abc") also raises ValueError.
#
# Convert input according to the expected data type.

# 3. DIVISION BY ZERO
# print(10 / 0)   # ZeroDivisionError
# Check the divisor before using /, //, or %.

# 4. INDENTATION
# The body of if, elif, else, loops, and functions
# must be indented correctly.

# 5. = VERSUS ==
# x = 5       # Assignment
# x == 5      # Equality comparison

# 6. STRINGS VERSUS NUMBERS
print("10" + "20")     # "1020"
print(10 + 20)         # 30

# 7. FLOATING-POINT PRECISION
# Some decimal numbers cannot be represented exactly
# in binary floating-point.
print(0.1 + 0.2)       # May display 0.30000000000000004

# For presentation, format the result:
print(f"{0.1 + 0.2:.2f}")  # 0.30

# 8. COMMENTS
# Use comments to explain intent or a non-obvious step.
# Avoid commenting every obvious line unnecessarily.

# 9. MEANINGFUL VARIABLE NAMES
# Prefer:
completed_credits = 100
#
# Over unclear names:
c = 100

# 10. TEST EDGE CASES
# For your calculator, test:
# - positive numbers
# - negative numbers
# - zero
# - a denominator of zero
#
# For your candy-sharing task, test:
# - total candies divisible by 3
# - total candies not divisible by 3
# - zero candies
