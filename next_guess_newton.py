# Part 1 - Task 4: Newton's method to find the cube root

x = float(input("What x to find the cube root of? "))
guess = float(input("What guess to start with? "))

# 1. Mevcut tahminin küpünü ekrana yazdır
current_cube = guess ** 3
print(f"Current estimate cube: {current_cube}")

# 2. Formüle göre bir sonraki tahmini hesapla: guess - (guess**3 - x) / (3 * guess**2)
next_guess = guess - (current_cube - x) / (3 * (guess ** 2))

# 3. Sonraki tahmini ekrana yazdır
print(f"Next guess: {next_guess}")