import numpy as np
temps = np.array(list(map(float, input("Enter temperature readings separated by space: ").split())))
print(f"Average Temperature: {np.mean(temps):.2f}°C")
print(f"Highest Temperature: {np.max(temps):.2f}°C")
print(f"Lowest Temperature: {np.min(temps):.2f}°C")
print(f"Variance: {np.var(temps):.2f}")
print(f"Standard Deviation: {np.std(temps):.2f}")
