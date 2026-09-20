n = int(input("Enter the number of leaves: "))
firststage = 0
secondstage = 1
print("Growth sequence:")
for i in range(n):
    print(firststage, end=" ")
    firststage, secondstage = secondstage, firststage + secondstage
