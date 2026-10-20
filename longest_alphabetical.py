# Part 4: Find the longest alphabetical substring

s = "azcbobobegghakl"

current = s[0]
longest = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        current += s[i]
    else:
        current = s[i]

    if len(current) > len(longest):
        longest = current

print("Longest substring in alphabetical order is:", longest)