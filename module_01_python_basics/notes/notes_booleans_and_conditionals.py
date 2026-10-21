
# ============================================================
# MODULE 1: BOOLEANS AND CONDITIONALS
# Topics: bool, comparisons, logical operators, if/elif/else,
#         truthy/falsy values, and operator precedence
# ============================================================


# ------------------------------------------------------------
# 1. BOOLEAN DATA TYPE
# ------------------------------------------------------------

# A Boolean (bool) has only two possible values:
# True and False.
# Remember: Python uses capital T and F.

is_student = True
has_paid_fee = False

print(is_student)
print(type(is_student))  # <class 'bool'>


# ------------------------------------------------------------
# 2. COMPARISON OPERATORS
# ------------------------------------------------------------

# Comparison operators compare values and return True or False.
#
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

age = 23

print(age >= 18)  # True
print(age == 18)  # False
print(age != 18)  # True

# A string and a number are different types.
print("3" == 3)       # False
print(int("3") == 3)  # True

# IMPORTANT:
# =  assigns a value
# == compares two values


# ------------------------------------------------------------
# 3. LOGICAL OPERATORS
# ------------------------------------------------------------

# and: True only when BOTH conditions are True.
# or:  True when AT LEAST ONE condition is True.
# not: Reverses a Boolean value.

age = 23
has_student_id = True

print(age >= 18 and has_student_id)  # True
print(age < 18 or has_student_id)    # True
print(not has_student_id)            # False

# Example: Both conditions must be satisfied.
attendance = 85
fee_paid = True

eligible = attendance >= 75 and fee_paid
print(eligible)  # True


# ------------------------------------------------------------
# 4. OPERATOR PRECEDENCE
# ------------------------------------------------------------

# Comparisons are evaluated before logical operators.
# 'not' is evaluated before 'and'.
# 'and' is evaluated before 'or'.

result = True or True and False
print(result)  # True

# Python evaluates the 'and' part first:
# True or (True and False)
# True or False
# True

# Use parentheses to make your intention clear.
result = (True or True) and False
print(result)  # False


# ------------------------------------------------------------
# 5. CONDITIONAL STATEMENTS
# ------------------------------------------------------------

# if: Runs a block when its condition is True.
# elif: Checks another condition if earlier ones were False.
# else: Runs when none of the previous conditions matched.

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs improvement")

# Python runs only the FIRST matching branch.
# The order of conditions therefore matters.

# Indentation defines which statements belong to a block.
if score >= 80:
    print("Passed")
    print("Good work!")

print("Assessment complete")  # Always runs


# ------------------------------------------------------------
# 6. TRUTHY AND FALSY VALUES
# ------------------------------------------------------------

# Python can interpret non-Boolean values as True or False.
#
# Common falsy values:
# 0, 0.0, "", [], (), {}, set(), None
#
# Most other values are truthy, including:
# Nonzero numbers, nonempty strings and nonempty collections.

print(bool(0))       # False
print(bool(25))      # True
print(bool(""))      # False
print(bool("False")) # True: this is a nonempty STRING!
print(bool([]))      # False
print(bool([1, 2]))  # True

# Example: Checking whether the user entered something.
name = input("Enter your name: ")

if name.strip():
    print(f"Hello, {name.strip()}!")
else:
    print("Name cannot be empty.")

# strip() removes whitespace at the beginning and end.
# Without strip(), an input of only spaces is still truthy.


# ------------------------------------------------------------
# 7. BOOLEAN FUNCTIONS
# ------------------------------------------------------------

# A function can return a Boolean value.

def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
print(is_adult(16))  # False

# return sends a value back to the caller.
# The function can then be used directly in a condition.

if is_adult(20):
    print("Eligible based on age.")
