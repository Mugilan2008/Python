import pandas as pd
n = int(input("Enter number of readings: "))
data = []
for i in range(n):
    panel = input("Enter panel type: ")
    time = input("Enter time of day: ")
    energy = float(input("Enter energy generated: "))
    data.append([panel, time, energy])
df = pd.DataFrame(data, columns=["Panel_Type", "Time", "Energy"])
table = pd.pivot_table(
    df,
    values="Energy",
    index="Panel_Type",
    columns="Time",
    aggfunc="sum",
    fill_value=0
)
print("\nPivot Table:")
print(table)
