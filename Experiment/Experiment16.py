n = int(input("Enter number of temperature readings: "))
limit = float(input("Enter temperature limit: "))
for i in range(n):
    temp = float(input("Enter temperature: "))
    print("Temperature =", temp)
    if temp > limit:
        print("WARNING: Temperature exceeded the limit")
    else:
        print("Temperature is normal")
