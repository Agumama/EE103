x = float(input("What x to find the square root of? "))
g = float(input("What guess to start with? "))

# Mevcut tahminin karesini yazdır
print(f"Current estimate square: {g ** 2}")

# Newton formülü: next_guess = g - (g^2 - x) / (2 * g)
next_guess = g - (g**2 - x) / (2 * g)

# Yeni tahmini yazdır
print(f"Next guess: {next_guess}")