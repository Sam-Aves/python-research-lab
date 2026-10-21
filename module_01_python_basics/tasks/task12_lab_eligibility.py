# Ask the user for their attendance percentage and whether their lab fee has been paid.

# Requirements:
# - Attendance must be between 0 and 100.
# - Attendance must be at least 75% to qualify.
# - The lab fee must be paid.
# - Display a different message if attendance is insufficient, the fee is unpaid, or both requirements are unmet.
# - Reject invalid attendance values.
# Concepts: Boolean variables, comparisons, and, if/elif/else, and input validation.

# Hint: Convert the fee response into a Boolean by checking whether the entered text matches an accepted answer such as "yes".
attendance = float(input("Enter your attendance percentage:"))
fee = float(input("Enter the lab fee amount: "))

if(attendance >=0 and attendance <= 100):
    if(attendance >=75 and fee > 0):
        print("You are eligible to take the lab.")
    elif(attendance >=75 and fee== 0):
        print("You must pay the lab fee to be eligible.")
    elif(attendance < 75 and fee > 0):
        print("Your attendance is insufficient to be eligible for the lab.")
    else:
        print("You do not meet the attendance and fee requirements to be eligible for the lab.")

else:
    print("Invalid attendance value. Please enter a percentage between 0 and 100.")
            
        