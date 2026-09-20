import pandas as pd
n = int(input("Enter number of equipment: "))
data = []
for i in range(n):
    name = input("Enter equipment name: ")
    voltage = float(input("Enter voltage: "))
    current = float(input("Enter current: "))
    pf = float(input("Enter power factor: "))
    data.append([name, voltage, current, pf])
df = pd.DataFrame(
    data,
    columns=["Equipment", "Voltage", "Current", "Power_Factor"]
)
df["Apparent_Power"] = df.eval("Voltage * Current / 1000")
df["Useful_Power"] = df.eval("Apparent_Power * Power_Factor")
limit = float(input("Enter power factor limit: "))
result = df.query("Power_Factor < @limit")
print("\nEquipment below the limit:")
print(result)
