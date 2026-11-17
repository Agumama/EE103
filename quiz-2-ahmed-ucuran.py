given_number = int(input("student Id:"))

if given_number < 0:
    print("square root of negative numb")

else:
    guess_number = 1
    while guess_number**2 < given_number:
        guess_number += 1
 if guess_number ** 2  == given_number:
    print(f"The square root of {given_number}is{guess_number}")

else:
    print(f"")