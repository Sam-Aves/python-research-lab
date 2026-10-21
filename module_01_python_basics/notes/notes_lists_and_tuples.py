
# ============================================================
# PYTHON NOTES: LISTS, METHODS, OBJECTS, AND TUPLES
# Module 01 - Python Basics
# ============================================================


# ------------------------------------------------------------
# 1. CREATING LISTS
# ------------------------------------------------------------

# A list stores an ordered sequence of values.
# Lists use square brackets [].

primes = [2, 3, 5, 7]

planets = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

# Lists can contain different data types.
mixed_list = [32, "Python", True, 3.14]

# A list can contain other lists.
hands = [
    ["J", "Q", "K"],
    ["2", "2", "2"],
    ["6", "A", "K"],
]

print("Primes:", primes)
print("Planets:", planets)
print("Mixed list:", mixed_list)
print("Hands:", hands)


# ------------------------------------------------------------
# 2. INDEXING
# ------------------------------------------------------------

# Python uses zero-based indexing.
# The first element is at index 0.

print(planets[0])    # Mercury
print(planets[1])    # Venus
print(planets[2])    # Earth

# Negative indexing starts from the end.
print(planets[-1])   # Neptune
print(planets[-2])   # Uranus

# Indexing a nested list.
print(hands[0])      # ['J', 'Q', 'K']
print(hands[0][1])   # Q

# An invalid index raises IndexError.


# ------------------------------------------------------------
# 3. SLICING
# ------------------------------------------------------------

# Syntax: list[start:stop]
# The start index is included.
# The stop index is excluded.

print(planets[0:3])    # First three planets
print(planets[:3])     # Same result: start defaults to 0
print(planets[3:])     # Index 3 through the end
print(planets[1:-1])   # All except the first and last
print(planets[-3:])    # Last three planets
print(planets[:])      # A shallow copy of the list

# Slicing does not raise IndexError just because the
# stop index is beyond the list's length.
print(planets[0:100])


# ------------------------------------------------------------
# 4. LISTS ARE MUTABLE
# ------------------------------------------------------------

# Mutable means an object can be changed after creation.

planets[3] = "Malacandra"
print(planets)

# Restore the original value.
planets[3] = "Mars"

# Slice assignment can replace multiple elements.
planets[:3] = ["Mur", "Vee", "Ur"]
print(planets)

# Restore the original first three elements.
planets[:3] = ["Mercury", "Venus", "Earth"]

# Slice assignment can change the list's length, too.
sample = [1, 2, 3, 4]
sample[1:3] = [20, 30, 40]
print(sample)  # [1, 20, 30, 40, 4]


# ------------------------------------------------------------
# 5. USEFUL BUILT-IN FUNCTIONS
# ------------------------------------------------------------

print(len(planets))       # Number of elements
print(sorted(planets))    # New sorted list; original unchanged
print(sum(primes))        # Sum of numeric elements
print(min(primes))        # Smallest value
print(max(primes))        # Largest value

# sorted() returns a new list.
# It does not sort the original list in place.

numbers = [4, 1, 3, 2]
sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted copy:", sorted_numbers)


# ------------------------------------------------------------
# 6. OBJECTS, ATTRIBUTES, AND METHODS
# ------------------------------------------------------------

# An object can have:
# - Attributes: data associated with the object.
# - Methods: functions associated with the object.

number = 12

print(number.imag)          # Attribute: imaginary part
print(number.bit_length())  # Method: number of bits needed
                            # to represent the integer in binary

# A method is called using dot syntax:
# object.method(arguments)

# help() can explain a method.
# Uncomment this line to inspect the method:
# help(number.bit_length)


# ------------------------------------------------------------
# 7. LIST METHODS: append() AND pop()
# ------------------------------------------------------------

planets.append("Pluto")
print(planets)

# append() adds one item to the end of the list.
# It modifies the list and returns None.

result = planets.append("Example")
print(result)   # None

# Remove the example item so the list stays tidy.
planets.pop()
print(planets)

# pop() removes AND returns an element.
removed_planet = planets.pop()
print("Removed:", removed_planet)
print("Remaining:", planets)

# pop(index) removes the element at a chosen index.
numbers = [10, 20, 30]
removed_number = numbers.pop(1)

print(removed_number)  # 20
print(numbers)         # [10, 30]


# ------------------------------------------------------------
# 8. SEARCHING A LIST
# ------------------------------------------------------------

planets = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

# index() returns the index of the first matching value.
print(planets.index("Earth"))  # 2

# If the value is absent, index() raises ValueError.
# Check membership first when necessary.

print("Earth" in planets)        # True
print("Pluto" in planets)        # False

if "Pluto" in planets:
    print(planets.index("Pluto"))
else:
    print("Pluto is not in the list.")

# Other useful membership checks:
print(5 in [1, 3, 5, 7])
print("Python" not in ["Java", "C++"])


# ------------------------------------------------------------
# 9. OTHER USEFUL LIST METHODS
# ------------------------------------------------------------

numbers = [3, 1, 2, 1]

numbers.append(4)       # Add one item
print(numbers)

numbers.extend([5, 6])  # Add multiple items from an iterable
print(numbers)

numbers.insert(1, 99)   # Insert at a chosen index
print(numbers)

numbers.remove(99)      # Remove the first matching value
print(numbers)

numbers.sort()          # Sort the original list in place
print(numbers)

numbers.reverse()       # Reverse the original list in place
print(numbers)

# clear() removes every element.
# numbers.clear()
# print(numbers)

# IMPORTANT:
# sort() modifies the list and returns None.
# sorted(list) returns a new sorted list.
# append(), extend(), insert(), remove(), reverse(),
# and sort() modify the list in place.


# ------------------------------------------------------------
# 10. TUPLES
# ------------------------------------------------------------

# Tuples are ordered sequences, like lists.
# They use parentheses or commas and are immutable.

coordinates = (10, 20, 30)
another_tuple = 1, 2, 3

print(coordinates)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:])

# A one-element tuple needs a trailing comma.
single_item_tuple = (5,)
print(single_item_tuple)

# Tuples cannot have their elements reassigned.
# coordinates[0] = 100  # Raises TypeError

# A tuple containing a mutable object can still contain
# an object that changes internally. Immutability means
# the tuple's own element references cannot be reassigned.


# ------------------------------------------------------------
# 11. MULTIPLE RETURN VALUES AND UNPACKING
# ------------------------------------------------------------

# A function can return multiple values separated by commas.
# Python packages them into a tuple.

def get_min_max(numbers):
    return min(numbers), max(numbers)


result = get_min_max([4, 8, 2, 10])
print(result)  # (2, 10)

# Unpack the returned tuple into separate variables.
smallest, largest = get_min_max([4, 8, 2, 10])

print("Smallest:", smallest)
print("Largest:", largest)

# The same idea works with other iterables of matching length.
first, second, third = ["A", "B", "C"]
print(first, second, third)


# ------------------------------------------------------------
# 12. SWAPPING VARIABLES
# ------------------------------------------------------------

a = 1
b = 0

# Python evaluates the right-hand side before assigning
# the values to the variables on the left.
a, b = b, a

print(a, b)  # 0 1

# This swaps the values without needing a temporary variable.


# ------------------------------------------------------------
# END OF NOTES
# ------------------------------------------------------------
