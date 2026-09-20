import pandas as pd
n = int(input("Enter number of passengers: "))
data = []
for i in range(n):
    pclass = int(input("Enter passenger class: "))
    survived = int(input("Enter survived (0 or 1): "))
    fare = float(input("Enter fare: "))
    data.append([pclass, survived, fare])
df = pd.DataFrame(data, columns=["Pclass", "Survived", "Fare"])
table = pd.pivot_table(
    df,
    values="Fare",
    index="Pclass",
    columns="Survived",
    aggfunc="mean"
)
print("\nPivot Table:")
print(table)
