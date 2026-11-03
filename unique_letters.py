# 1) Ask user for year input
year_str = input("What year is this? ")
year = int(year_str)

# 2) Extract each digit, cast to int, and sum them up using a for loop
total_sum = 0
for digit in year_str:
    total_sum += int(digit)

# 3) Divide the sum by the number of digits in the year input
average = total_sum / len(year_str)

print(f"Sum of digits: {total_sum}")
print(f"Average of digits: {average}")