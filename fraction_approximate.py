# Part 9: Approximate binary conversion for repeating fractions (e.g., 0.1)

target = 0.1
fraction = target
tolerance = 0.00001

binary_str = "0."
current_value = 0.0
power = 1  # 2^-1, 2^-2, 2^-3 adımlarını takip eder

while abs(current_value - target) >= tolerance:
    fraction = fraction * 2
    integer_part = int(fraction)
    binary_str += str(integer_part)
    
    # Elde edilen ikilik basamağın onluk değere katkısını ekliyoruz
    current_value += integer_part * (2 ** (-power))
    
    fraction = fraction - integer_part
    power += 1

print(f"Target: {target}")
print(f"Binary representation: {binary_str}")
print(f"Approximated decimal value: {current_value}")
print(f"Final error: {abs(current_value - target)}")