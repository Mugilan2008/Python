k = int(input("Enter number of rows: "))
for n in range(k):
    value = 1
    for r in range(n + 1):
        print(value, end=" ")
        value = value * (n - r) // (r + 1)
    print()
