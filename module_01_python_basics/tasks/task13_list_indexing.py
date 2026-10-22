# Task 11 — List Indexing
# Given this list:
# programming_languages = [
#     "Python", "C++", "Java", "JavaScript",
#     "Go", "Rust", "C"
# ]Requirements
# 1. Print the first programming language.
# 2. Print the third programming language.
# 3. Print the last programming language using a negative index.
# 4. Print the second-to-last programming language using a negative index.
# 5. Print the element at index 3.
# 6. Print the length of the list.
# 7. Predict what happens when you try to access index 10, then test it.

# Hints
# - Remember that indexing starts at 0.
# - Negative indexing starts at -1 for the last element.
# - Use len() to find the number of elements.
# - For the final requirement, don't just guess—run the code and read the error.
programming_languages = [
    "Python", "C++", "Java", "JavaScript",
    "Go", "Rust", "C",
]
#1
print(programming_languages[0])

#2
print(programming_languages[2])

#3
print(programming_languages[-1])

#4
print(programming_languages[-2])

#5
print(programming_languages[3])

#6
print(len(programming_languages))

#7
#print(programming_languages[10])