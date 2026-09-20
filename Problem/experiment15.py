n = int(input("Enter number of readings: "))
rated = float(input("Enter rated current: "))
for i in range(n):
    current = float(input("Enter current: "))
    if current > rated:
        print(current, "-> OVERLOAD WARNING")
    else:
        print(current, "-> Normal")
