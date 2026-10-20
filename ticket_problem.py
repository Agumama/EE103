# Part 4: Ticket problem using Guess and Check with nested loops

total_tickets = 10
found = False

# Alyssa, Ben ve Cindy'nin satabileceği olası bilet sayılarını 0'dan 10'a kadar deniyoruz
for alyssa in range(total_tickets + 1):
    for ben in range(total_tickets + 1):
        for cindy in range(total_tickets + 1):
            # Koşullarımız:
            # 1. Ben, Alyssa'dan 2 eksik satmalı
            # 2. Cindy, Alyssa'nın 2 katı satmalı
            # 3. Üçünün toplamı 10 etmeli
            if (ben == alyssa - 2) and (cindy == 2 * alyssa) and (alyssa + ben + cindy == total_tickets):
                print(f"Alyssa sold {alyssa} tickets.")
                print(f"Ben sold {ben} tickets.")
                print(f"Cindy sold {cindy} tickets.")
                found = True
                break
        if found:
            break
    if found:
        break