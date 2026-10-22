#List Comprehension for Data Cleaning
# Practise: list comprehensions, filtering, transforming data

# Suppose you have a list of raw values representing ages:
#     ages = [21, 19, -1, 23, 0, 22, 150, 20, -5, 24]
# For this exercise, assume valid ages are between 1 and 100 inclusive.

# Write code to:
# 1. Create a new list containing only valid ages, using a list comprehension.
# 2. Create another list containing the valid ages converted to strings, using a list comprehension.
# 3. Create a list of only the valid ages that are at least 21.
# 4. Print the original list and all three new lists to confirm that the original data hasn't changed.
# Hint for filtering:
# # General pattern — fill in the expression and condition yourself
# new_list = [expression for item in original_list if condition]

ages = [21, 19, -1, 23, 0, 22, 150, 20, -5, 24]
#1
valid_age = [age for age in ages if age >= 1 and age <= 100]
print(valid_age)

#2
valid_age_string = [str(age) for age in valid_age]
print(valid_age_string)

#3
valid_age_21 = [age for age in valid_age if age >= 21]
print(valid_age_21)

print("Original list:", ages)
print("Valid ages:", valid_age)
print("String valid ages: ", valid_age_string)
print("Valid age at least 21 years old:", valid_age_21)