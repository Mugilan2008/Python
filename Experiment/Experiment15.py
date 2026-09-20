n = int(input("Enter number of heart rate readings: "))
low = int(input("Enter minimum heart rate: "))
high = int(input("Enter maximum heart rate: "))
for i in range(n):
    rate = int(input("Enter heart rate: "))
    if rate < low or rate > high:
        print(rate, "-> WARNING: Outside range")
    else:
        print(rate, "-> Normal")
