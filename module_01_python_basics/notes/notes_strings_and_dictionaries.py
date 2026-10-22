
# ============================================================
# MODULE 1: PYTHON BASICS
# Topic: Strings and Dictionaries
# ============================================================


# ============================================================
# 1. STRINGS
# ============================================================

# A string is a sequence of characters.
# Strings can use single or double quotes.

name = "Python"
message = 'Python is useful for machine learning'

print(name)
print(message)

# Use different quote types when a string contains an apostrophe.
print("Python's syntax is readable")
print('She said, "Hello!"')

# Escape characters let us include special characters.
print("It's Python!")       # Apostrophe inside double quotes
print('It\'s Python!')      # Escaped apostrophe
print("Hello\nWorld")       # \n creates a new line
print("Path: C:\\Users")    # \\ represents a backslash


# Triple quotes can create multiline strings.
paragraph = """Python is useful.
It is widely used in data science.
It is also used in machine learning."""

print(paragraph)


# ============================================================
# 2. STRINGS AS SEQUENCES
# ============================================================

# Strings support indexing, slicing, len(), and loops.

language = "Python"

print(language[0])       # First character: P
print(language[-1])      # Last character: n
print(language[1:4])     # Characters at indices 1, 2, 3
print(language[-3:])     # Last three characters
print(len(language))    # Number of characters

# Loop through characters.
for char in language:
    print(char)

# IMPORTANT:
# Strings are immutable. You cannot change an individual
# character in place.

# language[0] = "J"      # Raises TypeError

# Instead, create a new string.
language = "J" + language[1:]
print(language)          # Jython


# ============================================================
# 3. USEFUL STRING METHODS
# ============================================================

text = "  Python for Machine Learning  "

print(text.lower())       # Convert to lowercase
print(text.upper())       # Convert to uppercase
print(text.strip())       # Remove surrounding whitespace
print(text.replace("Python", "Data Science"))

# Search for text.
claim = "Machine learning uses data"

print(claim.find("learning"))       # Starting index, or -1
print(claim.startswith("Machine"))  # True
print(claim.endswith("data"))       # True

# .index() also searches for a substring,
# but raises ValueError if it cannot find it.
print(claim.index("data"))

# Check whether a string contains a substring.
print("learning" in claim)          # True


# ============================================================
# 4. SPLIT AND JOIN
# ============================================================

# .split() converts a string into a list of strings.
sentence = "Python is useful for ML"
words = sentence.split()

print(words)
# ['Python', 'is', 'useful', 'for', 'ML']

# Split using a specific separator.
date = "2026-10-23"
year, month, day = date.split("-")

print(year)
print(month)
print(day)

# .join() combines strings using a separator.
joined = " ".join(words)
print(joined)

print(", ".join(words))

# IMPORTANT:
# join() expects an iterable of strings, not integers.


# ============================================================
# 5. FORMATTING STRINGS
# ============================================================

# F-strings are a convenient way to insert values into strings.

student = "Ayesha"
score = 92

print(f"{student} scored {score}")

average = 87.456
print(f"Average: {average:.2f}")    # Two decimal places

population = 52910390
print(f"Population: {population:,}")  # Thousands separators

# The .format() method is another way to format strings.
print("{} scored {}".format(student, score))

# Both f-strings and .format() can insert numbers
# without manually converting them using str().


# ============================================================
# 6. DICTIONARIES
# ============================================================

# A dictionary stores key-value pairs.
# Syntax: {key: value}

student = {
    "name": "Ayesha",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.998
}

print(student)

# Access a value using its key.
print(student["name"])
print(student["cgpa"])

# Add a new key-value pair.
student["semester"] = 7

# Update an existing value.
student["cgpa"] = 4.00

print(student)

# Keys must be unique. Assigning a value to an existing key
# updates that key instead of creating a duplicate.


# ============================================================
# 7. ACCESSING DICTIONARY VALUES SAFELY
# ============================================================

# Accessing a missing key with [] raises KeyError.

# print(student["email"])  # Raises KeyError

# .get() safely retrieves a value.
print(student.get("name"))
print(student.get("email"))          # Returns None
print(student.get("email", "N/A"))   # Returns "N/A"

# Check whether a key exists.
print("name" in student)             # True
print("email" in student)            # False

# IMPORTANT:
# The 'in' operator checks dictionary KEYS, not values.


# ============================================================
# 8. LOOPING THROUGH DICTIONARIES
# ============================================================

# Looping directly through a dictionary gives its keys.
for key in student:
    print(key, student[key])

# .keys() gives the keys.
print(student.keys())

# .values() gives the values.
print(student.values())

# .items() gives key-value pairs.
for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 9. DICTIONARY COMPREHENSIONS
# ============================================================

# Similar to list comprehensions, but create dictionaries.

planets = ["Mercury", "Venus", "Earth", "Mars"]

# Each planet becomes a key; its first character is the value.
planet_initials = {
    planet: planet[0]
    for planet in planets
}

print(planet_initials)

# General pattern:
# {key_expression: value_expression for item in iterable}

# Example: map numbers to their squares.
numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ============================================================
# 10. WHY THESE TOPICS MATTER FOR DATA SCIENCE
# ============================================================

# Strings:
# - Clean text with strip(), lower(), and replace()
# - Split text into smaller parts
# - Format readable output
# - Inspect and transform text columns

# Dictionaries:
# - Represent structured records
# - Map categories to values
# - Count occurrences or store lookup information
# - Understand data structures encountered in Python code

# Example: Count category occurrences using a dictionary.
categories = ["plastic", "paper", "plastic", "metal", "paper"]

counts = {}

for category in categories:
    if category in counts:
        counts[category] += 1
    else:
        counts[category] = 1

print(counts)
# {'plastic': 2, 'paper': 2, 'metal': 1}

# This is a basic example of counting categorical data.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Strings are immutable sequences of characters.
# 2. Indexing and slicing work on strings, just as with lists.
# 3. split() converts a string into a list.
# 4. join() combines strings into one string.
# 5. f-strings make formatting easy and readable.
# 6. Dictionaries store key-value pairs.
# 7. Use [] to access known keys and get() for safer lookups.
# 8. Use .items() to loop over keys and values together.
# 9. Dictionary comprehensions create dictionaries concisely.
