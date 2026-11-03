# Part 2: Demonstrate Floating Error

# 1) Define variables x and y
x = 0.1
y = 0.2

# 2) Define result
result = x + y
print(f"Calculated result (x + y): {result}")

# 3) Check if result is exactly equal to 0.3
exact_check = (result == 0.3)
print(f"Is result == 0.3? -> {exact_check}")

# 4) Check if it is close enough within epsilon margin (1e-4)
epsilon = 1e-4
close_check = (0.3 - epsilon <= result <= 0.3 + epsilon)
print(f"Is result close enough to 0.3? -> {close_check}")