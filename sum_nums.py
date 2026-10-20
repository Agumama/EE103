# Part 6: Running Sum and Gauss summation

n = int(input("Enter a number: "))

# 1. Döngü ile toplam hesaplama
running_sum = 0
for i in range(1, n + 1):
    running_sum += i

# 2. Gauss formülü ile hesaplama: n * (n + 1) / 2
sum_gauss = n * (n + 1) // 2

print(f"Loop sum: {running_sum}")
print(f"Gauss sum: {sum_gauss}")

# 3. Kontrol ve sonuç yazdırma
if running_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")