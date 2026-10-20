# Part 6: Floating Point Precision Issue

x = 0
for i in range(10):
    print(x)
    x = x + 0.1

print("Final value of x:", x)