import pandas as pd
n = int(input("Enter number of employees: "))
data = []
for i in range(n):
    name = input("Enter employee name: ")
    regular = float(input("Enter regular hours: "))
    overtime = float(input("Enter overtime hours: "))
    data.append([name, regular, overtime])
df = pd.DataFrame(
    data,
    columns=["Name", "Regular_Hours", "Overtime_Hours"]
)
df["Total_Hours"] = df.eval("Regular_Hours + Overtime_Hours")
limit = float(input("Enter hour limit: "))
result = df.query("Total_Hours > @limit")
print("\nEmployees:")
print(result)
