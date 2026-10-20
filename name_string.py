s = "Aho54yuAHMED42z.89tur"

# "Aho54yu" kısmı 7 karakterdir (indeks 0'dan 6'ya kadar).
# "AHMED" kısmı indeks 7'den başlar ve 12'ye kadar sürer (7:12).
my_name = s[7:12]

# Ters çevirmek için adım değerine -1 veriyoruz (slice: [::-1])
reverse_name = my_name[::-1]

print(f"My name is {my_name}")
print(f"My name in reverse order is {reverse_name}")