# Part 2: Guess number script
from secret_number import secretNum

user_guess = int(input("Enter your guess: "))

if user_guess < secretNum:
    print("Your guess is too low!")
elif user_guess > secretNum:
    print("Your guess is too high!")
else:
    print("Congratulations! Your guess is the same as the secret number!")