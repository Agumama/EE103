# find_secret_bisection_search.py
from secret_data import secret_year

low_bound = 0
high_bound = 2026
num_guesses = 1
guess = (low_bound + high_bound) // 2

while guess != secret_year:
    if guess < secret_year:
        low_bound = guess + 1
    else:
        high_bound = guess - 1
        
    guess = (low_bound + high_bound) // 2
    num_guesses += 1

print("--- Bisection Search ---")
print(f"Secret year found: {guess}")
print(f"Total number of guesses: {num_guesses}")