# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

alice_candies = int(input("Enter the number of candies Alice has: "))
bob_candies = int(input("Enter the number of candies Bob has: "))
carol_candies = int(input("Enter the number of candies Carol has: "))

total = alice_candies + bob_candies + carol_candies
print("Smashed candies:", total % 3)
