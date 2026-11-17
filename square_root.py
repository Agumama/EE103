
given_number = int(input("Enter an integeroot: "))

if given_number < 0:
    print("Square not .")
else:
    guess_number = 1
    while guess_number ** 2 < given_number:
        guess_number += 1

    if guess_number ** 2 == given_number:
        print(f"The square root of {given_number} is {guess_number}")
    else:
        print(f"{given_number} is not a perfect square.")