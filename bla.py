# 1. Kullanıcıdan pozitif bir tam sayı (n) al ve int'e çevir
n = int(input("Enter n: "))

# 2. total = 0.0'dan başlayarak, for döngüsüyle n kere 0.1 ekle
total = 0.0
for i in range(n):
    total += 0.1

# 3. total değerini yazdır
print(total)

# 4. İki karşılaştırmanın sonucunu (True/False) etiketleriyle yazdır
print("equal:", total == n / 10)
print("close enough:", abs(total - n / 10) < 1e-9)