# Part 3: Count unique letters in a string

s = "ece"
unique_chars = ""

for char in s:
    if char not in unique_chars:
        unique_chars += char

count = len(unique_chars)
print(f"Number of unique letters in '{s}' is: {count}")