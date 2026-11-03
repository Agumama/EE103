# sqrt_bisection_search.py
from secret_data import secret_number

epsilon = 0.01
num_guesses = 0
low = 0.0
high = max(1.0, float(secret_number))
guess = (low + high) / 2.0

while abs(guess**2 - secret_number) >= epsilon:
    num_guesses += 1
    if guess**2 < secret_number:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0

print("--- Square Root: Bisection Search ---")
print(f"Target number: {secret_number}")
print(f"Calculated square root: {guess:.4f}")
print(f"Total number of guesses: {num_guesses}")