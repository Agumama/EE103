# sqrt_approximation.py
from secret_data import secret_number

epsilon = 0.01
step = 0.001
guess = 0.0
num_guesses = 0

# Increment guess by step until guess^2 is close enough or overshoots
while abs(guess**2 - secret_number) >= epsilon and guess**2 <= secret_number:
    guess += step
    num_guesses += 1

print("--- Square Root: Approximation Method ---")
print(f"Target number: {secret_number}")
if abs(guess**2 - secret_number) >= epsilon:
    print("Failed to find square root within step and epsilon bounds.")
else:
    print(f"Approximated square root: {guess:.4f}")
print(f"Total number of guesses: {num_guesses}")