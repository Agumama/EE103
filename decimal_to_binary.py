# Part 7: Convert decimal integer to binary

num = 13
original_num = num

if num == 0:
    binary_str = "0"
else:
    remainders = ""
    while num > 0:
        remainder = num % 2
        remainders += str(remainder)
        num = num // 2

    # Kalanları tersten sıralayarak ikilik sayıyı elde ediyoruz
    binary_str = remainders[::-1]

print(f"{original_num} converted to binary is: {binary_str}")