
# ==========================================
# ARITHMETIC OPERATORS AND EXPRESSIONS
# ==========================================

# An expression combines values, variables, and operators
# to produce a result.

a = 10
b = 3

# Addition
print(a + b)       # 13

# Subtraction
print(a - b)       # 7

# Multiplication
print(a * b)       # 30

# Division: produces a floating-point result.
print(a / b)       # Approximately 3.3333

# Floor division: rounds the quotient down.
print(a // b)      # 3

# Modulo: gives the remainder after division.
print(a % b)       # 1

# Exponentiation: raises a number to a power.
print(a ** b)      # 1000

# ------------------------------------------
# WHEN ARE THESE OPERATORS USEFUL?
# ------------------------------------------

# Modulo can check whether a number is even or odd.
number = 8
print(number % 2)  # 0 means even; 1 means odd

# Modulo can calculate a remainder after sharing.
candies = 14
people = 3

print(candies // people)  # 4 candies per person
print(candies % people)   # 2 candies left over

# Division versus floor division:
print(7 / 2)       # 3.5
print(7 // 2)      # 3

# For negative numbers, floor division rounds toward
# negative infinity, not simply toward zero.
print(-7 // 2)     # -4

# ------------------------------------------
# COMPOUND EXPRESSIONS
# ------------------------------------------

x = 5
y = 3

result = x * y + 2
print(result)      # 17

# Expressions can be stored in variables.
total = 10 + 20 + 30
average = total / 3

print(total)
print(average)

# Python can evaluate expressions directly in print().
print(10 + 5)
print(2 ** 3)

# Be careful when dividing by zero:
# /, //, and % with a zero divisor raise ZeroDivisionError.
