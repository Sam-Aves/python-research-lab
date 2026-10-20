
# ==========================================
# INPUT, OUTPUT, TYPE CONVERSION, AND F-STRINGS
# ==========================================

# input() displays a prompt and receives user input.
# IMPORTANT: input() always returns a string (str).

name = input("Enter your name: ")
print(name)

# Convert input into an integer using int().
age = int(input("Enter your age: "))

# Convert input into a floating-point number using float().
cgpa = float(input("Enter your CGPA: "))

print(type(name))          # str
print(type(age))           # int
print(type(cgpa))          # float

# Conversion is necessary when performing numerical calculations.
# Otherwise, + may join strings instead of adding numbers.

first = "10"
second = "20"

print(first + second)      # Output: 1020 (string concatenation)
print(int(first) + int(second))  # Output: 30

# Invalid conversions can raise ValueError.
# For example, int("hello") is invalid.

# ------------------------------------------
# PRINTING OUTPUT
# ------------------------------------------

print("Hello")
print("Python", "is", "fun")

# f-strings allow variables and expressions inside strings.
# Put f before the opening quotation mark.
# Place variables or expressions inside curly braces {}.

name = "Alice"
score = 95

print(f"My name is {name}.")
print(f"My score is {score}.")
print(f"Next year's score could be {score + 2}.")

# You can perform calculations inside an f-string.
a = 10
b = 3
print(f"The sum is {a + b}.")

# Formatting a float to two decimal places:
pi = 3.14159265
print(f"Pi is approximately {pi:.2f}")

# :.2f means display the number with two digits after the decimal.
# It changes how the number is displayed, not its stored value.

# ------------------------------------------
# PRINT PARAMETERS: sep AND end
# ------------------------------------------

# sep controls what appears between multiple printed values.
print("2026", "10", "20", sep="-")
# Output: 2026-10-20

print("Alice", "Bob", "Carol", sep=", ")
# Output: Alice, Bob, Carol

# end controls what appears at the end of a print statement.
# By default, print() ends with a newline: end="\n".

print("Hello", end=" ")
print("World")
# Output: Hello World

# Comments begin with # and are ignored by Python.
# Use comments to explain why code works or what it does.
