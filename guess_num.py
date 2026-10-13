# Part 4: Infinite Loops after 5 wrong guesses
from secret_number import secretNum

guess_count = 0

while True:
    user_guess = int(input("Enter your guess: "))
    guess_count += 1
    
    if user_guess == secretNum:
        print("Congratulations! Your guess is the same as the secret number!")
        break
    elif user_guess < secretNum:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
        
    # 5. denemeden sonra hala bulunamadıysa sonsuz döngüye gir
    if guess_count == 5:
        while True:
            print("Oh! Noooooo...")