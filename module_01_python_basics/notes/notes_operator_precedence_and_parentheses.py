
# ==========================================
# OPERATOR PRECEDENCE AND PARENTHESES
# ==========================================

# Operator precedence determines which operations
# are evaluated first in an expression.

# A simplified precedence order for our current tasks:
#
# 1. Parentheses:       ()
# 2. Exponentiation:    **
# 3. Multiplication, division, floor division, modulo:
#                       *, /, //, %
# 4. Addition, subtraction:
#                       +, -
#
# Operators at the same level are generally evaluated
# from left to right, except exponentiation, which
# groups from right to left.

# ------------------------------------------
# EXAMPLES
# ------------------------------------------

print(2 + 3 * 4)       # 14, not 20
# Multiplication happens before addition.

print((2 + 3) * 4)     # 20
# Parentheses make addition happen first.

print(2 ** 3 * 2)      # 16
# Exponentiation happens before multiplication.

print(2 ** (3 * 2))    # 64
# Parentheses change the order of evaluation.

print(10 - 4 - 2)      # 4
# Subtraction is evaluated from left to right.

print(2 ** 3 ** 2)     # 512
# Exponentiation groups from right to left:
# 2 ** (3 ** 2) = 2 ** 9 = 512

# ------------------------------------------
# WHY PARENTHESES MATTER IN FORMULAS
# ------------------------------------------

# Temperature conversion:
# Fahrenheit = (9 / 5 * Celsius) + 32

celsius = 25
fahrenheit = (9 / 5) * celsius + 32
print(fahrenheit)      # 77.0

# Circle area:
# Area = pi * radius squared

pi = 3.1416
radius = 5
area = pi * (radius ** 2)
print(area)

# CGPA estimation uses a weighted average.
# Each CGPA is multiplied by its corresponding credits.
# The combined weighted total is divided by total credits.

old_cgpa = 3.9
old_credits = 100
semester_cgpa = 4.0
semester_credits = 20

updated_cgpa = (
    (old_cgpa * old_credits)
    + (semester_cgpa * semester_credits)
) / (old_credits + semester_credits)

print(updated_cgpa)

# Best practice:
# Use parentheses to make complicated formulas easier to read,
# even when Python's precedence rules already give the right result.
