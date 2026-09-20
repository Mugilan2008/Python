import numpy as np
voltages = np.array(list(map(float, input("Enter cell voltages separated by space: ").split())))
print(f"First Cell Voltage: {voltages[0]} V")
print(f"Last Cell Voltage: {voltages[-1]} V")
sorted_v = np.sort(voltages)
print("Sorted Voltages:", sorted_v)
print(f"Lowest Cell Voltage: {sorted_v[0]} V")
print(f"Highest Cell Voltage: {sorted_v[-1]} V")
