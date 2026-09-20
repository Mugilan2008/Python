n = int(input("Enter the number of sensor numbers: "))
even = []
odd = []
for i in range(n):
    num = int(input("Enter the sensor number: "))
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even sensor numbers:", even)
print("Odd sensor numbers:", odd)
