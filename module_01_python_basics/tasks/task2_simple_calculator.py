num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Addition
print(f"Summation of the two numbers is {num1 + num2}. ")

#Subtraction
print(f"Subtraction of the two numbers is {num1 - num2}. ")

#Multiplication
print(f"Multiplication of the two numbers is {num1 * num2}. ")
if num2 != 0: 
    #Division
    print(f"Division of the two numbers is {num1 / num2}. ")
    #Integer division
    print(f"Integer Division of the two numbers is {num1 // num2}. ")
    #Modulo
    print(f"Mod of the two numbers is {num1 % num2}. ")
else:
    print("Division and Modulo by 0 not allowed. ")
#Exponentiation
print(f"{num1} raised to the power of {num2} is {num1 ** num2}. ")