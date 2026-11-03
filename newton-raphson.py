# newton-raphson.py
from secret_data import secret_number

# 2) Error margin epsilon, initial guess, number of guesses
epsilon = 0.01
guess = secret_number / 2.0
num_guesses = 0

# 3) While loop with condition abs(guess*guess - secret_number) >= epsilon
while abs(guess * guess - secret_number) >= epsilon:
    # Newton-Raphson update step: guess = guess - (guess^2 - secret_number) / (2 * guess)
    guess = guess - (guess**2 - secret_number) / (2 * guess)
    num_guesses += 1

# e) Print number of guesses and calculated square root
print("--- Newton-Raphson Method ---")
print(f"Target number: {secret_number}")
print(f"Calculated square root: {guess:.4f}")
print(f"Total number of guesses: {num_guesses}")