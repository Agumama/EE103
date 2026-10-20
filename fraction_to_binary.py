# Part 8: Convert decimal fraction to binary

fraction = 0.375
original_fraction = fraction

binary_str = "0."

# Kesir tam sıfır olana kadar veya sonsuz döngüye girmemesi için en fazla 20 basamak hesapla
max_iterations = 20
count = 0

while fraction > 0 and count < max_iterations:
    fraction = fraction * 2
    integer_part = int(fraction)
    binary_str += str(integer_part)
    fraction = fraction - integer_part
    count += 1

print(f"{original_fraction} converted to binary is: {binary_str}")