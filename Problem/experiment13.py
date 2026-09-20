import matplotlib.pyplot as plt
n = int(input("Enter number of readings: "))
vds = []
id_value = []
for i in range(n):
    v = float(input("Enter VDS: "))
    current = float(input("Enter ID: "))
    vds.append(v)
    id_value.append(current)
plt.scatter(vds, id_value)
plt.xlabel("VDS")
plt.ylabel("ID")
plt.title("JFET Drain Characteristic (VGS = 0V)")
plt.show()
