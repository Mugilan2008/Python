even = []
odd = []
input_1 = []
n = int(input("Enter how many numbers: "))
for i in range(n):
    num = int(input("Enter number: "))
    input_1.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Elements in the List:", input_1)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
