n = int(input("Enter a number: "))
multiply = lambda x, y: x * y
for i in range(1, 11):
    print(n, "x", i, "=", multiply(n, i))
