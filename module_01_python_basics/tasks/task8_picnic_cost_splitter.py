# Task 8 — Picnic Cost Splitter
# Your goal: Write a Python program that calculates the total picnic cost, how much each person should pay, and whether any money remains when the cost is shared equally.
# Requirements
# 1. Ask the user to enter the picnic costs paid by three friends.
# 2. Convert each input into a number so you can perform calculations.
# 3. Calculate the total cost using addition.
# 4. Calculate the cost per person using division.
# 5. Use the modulo operator (%) to find the remainder when the total cost is divided by 3.
# 6. Display the results using f-strings or print().
# Example run
# Example input and expected output

# Enter Alice's contribution: 100
# Enter Bob's contribution: 150
# Enter Carol's contribution: 200

# Total picnic cost: 450
# Cost per person: 150.0
# Remainder after division by 3: 0

Alice_contribution = float(input("Enter Alice's Contribution: "))
Bob_contribution = float(input("Enter Bob's Contribution: "))
Carol_contribution = float(input("Enter Carol's Contribution: "))

total =  Alice_contribution + Bob_contribution + Carol_contribution
print(f"Total picnic cost: {total:.2f}")

print(f"Cost per person: {total / 3:.2f}")

print(f"Remainder after division by 3: {total % 3:.2f}")
