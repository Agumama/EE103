# find_secret_guess_and_check.py
from secret_data import secret_year

guess = 0
num_guesses = 0

# Brute-force guess and check
while guess <= 2026:
    num_guesses += 1
    if guess == secret_year:
        break
    guess += 1

print("--- Guess and Check ---")
print(f"Secret year found: {guess}")
print(f"Total number of guesses: {num_guesses}")