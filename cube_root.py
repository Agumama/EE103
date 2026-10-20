# Part 8: Guess and check for cube root (both positive and negative)

num = int(input("Enter an integer to find its cube root: "))

# Negatif sayılar için mutlak değer üzerinden işlem yapıyoruz
abs_num = abs(num)
guess = 0

while guess ** 3 < abs_num:
    guess += 1

if guess ** 3 != abs_num:
    print(f"{num} is not a perfect cube.")
else:
    # Sayı negatifse küp kökünü de negatif yapıyoruz
    if num < 0:
        guess = -guess
    print(f"The cube root of {num} is {guess}")