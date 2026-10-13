# Part 7: Guess and check for square root

given_number = int(input("Enter an integer to find its square root: "))

# c) Negatif sayı kontrolü
if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess_number = 1
    # a) 1'den başlayıp karesi sayıdan küçük veya eşit olduğu sürece artır
    while guess_number ** 2 < given_number:
        guess_number += 1

    # b) Tam kare mi değil mi kontrolü
    if guess_number ** 2 == given_number:
        print(f"The square root of {given_number} is {guess_number}")
    else:
        print(f"{given_number} is not a perfect square.")