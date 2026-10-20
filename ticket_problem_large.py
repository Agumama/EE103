# Part 5: Ticket problem with 1000 tickets (Comparing efficiency)
import time

total_tickets = 1000

# Yöntem 1: Tek döngü (Single loop - Çok hızlı ve verimli)
start_time = time.time()

for alyssa in range(total_tickets + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa
    
    if (ben >= 0) and (alyssa + ben + cindy == total_tickets):
        print(f"Alyssa sold {alyssa} tickets.")
        print(f"Ben sold {ben} tickets.")
        print(f"Cindy sold {cindy} tickets.")
        break

end_time = time.time()
print(f"Elapsed time with single loop: {end_time - start_time:.6f} seconds")