# Dataset Analyzer
# Practise: for loops, if, range(), sum(), len(), min(), max()

# Imagine these are the exam scores of students in your class:
# scores = [78, 45, 92, 0, 67, 85, 38, 100, 56, 72]
# Write a program that:
# 1. Uses a for loop to print each score on a separate line.
# 2. Counts how many students passed. A passing score is 50 or above.
# 3. Counts how many students scored below 50.
# 4. Calculates the average score.
# 5. Prints the highest and lowest scores.
# 6. Uses range() to print the first three scores by their indices.
# Requirements: Use a loop for the pass/fail counts. Don't use a library or search for a solution.

# Hint: You can maintain a counter starting at 0 and increase it inside an if statement.


scores = [78, 45, 92, 0, 67, 85, 38, 100, 56, 72]
#1
for i in scores:
    print(i, end = " ")
#2
print()
passing_student = len([num for num in scores if num >= 50])
count = 0
for i in scores:
    if i >= 50:
        count += 1
print("Passed students: ", count)
print(f"Number of passing students: {passing_student}.")
#3
count = 0
for i in scores:
        if i < 50:
            count+=1
print("Failed students:", count)
failed_students = len([num for num in scores if num < 50])
print(f"Number of failed students: {failed_students}.")
#4
avg_score = sum(scores) / len(scores)
print(f"Average score: {avg_score}.")
#5
print(f"lowest score: {min(scores)}.")
print(f"Highest score: {max(scores)}.")

#6
print("Three first three scores are:")
for i in range(3):
    print(scores[i], end = " ")
print()




