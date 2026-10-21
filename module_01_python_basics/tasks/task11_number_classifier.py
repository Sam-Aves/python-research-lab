# Ask the user to enter a number. Your program must:
# 1. Identify whether the number is positive, negative or zero.
# 2. Determine whether it is even or odd.
# 3. Check whether it falls within the inclusive range 1–100.
# 4. Handle input that cannot be converted into a number without crashing.
# Concepts: Boolean comparisons, if/elif/else, and, or, modulo %, and try/except.

# Hint: Zero is even, but it is not within the range 1–100.


#4
try:
    num = int(input("Enter a number: "))
except:
    print("Invalid input. Please enter a valid integer.")
    exit()

#1
if(num > 0):
    print(num, "is a positive number.")
    
elif(num == 0):
    print(num, "is zero.")

else:
    print(num, "is a negative number.")
    
#2
if(num % 2 == 0):
    print(num, "is an even number.")
    
else:
    print(num, "is an odd number.")

#3
if(num >=1 and num <=100):
    print(num, "is within the range 1-100.")
else:
    print(num, "is not within the range 1-100.")
    