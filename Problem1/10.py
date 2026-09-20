a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))
missing = []
for x in b:
    if x not in a:
        missing.append(x)
print("Missing elements:", missing)
