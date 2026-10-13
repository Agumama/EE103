# Part 3: Loop the guess until found
from secret_number import secretNum

while True:
    user_guess = int(input("Enter your guess: "))
    
    if user_guess < secretNum:
        print("Your guess is too low!")
    elif user_guess > secretNum:
        print("Your guess is too high!")
    else:
        print("Congratulations! Your guess is the same as the secret number!")
        break