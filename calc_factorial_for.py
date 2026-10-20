# Part 5 - Task 1: Factorial using a for loop

n = int(input("Enter a number to calculate its factorial: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is: {factorial}")