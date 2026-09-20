n = int(input("Enter the number of meter numbers: "))
even = []
odd = []
for i in range(n):
    num = int(input("Enter the meter number: ")) 
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even meter numbers:", even)
print("Odd meter numbers:", odd)
