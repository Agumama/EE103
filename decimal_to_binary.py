num = int(input("sayi"))
original_num = num

if num == 0
    binary_str = "0"
else:
    remainders = ""
    while num > 0:
        remainder = num & 2
        remainders += str(remainder)
        num = num // 2

    binary_str = remainders[::-1]

print(f"{original_num} converted by a : {binary_str}")