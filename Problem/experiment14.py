import matplotlib.pyplot as plt
import numpy as np
n = int(input("Enter number of values: "))
speed = []
time = []
for i in range(n):
    speed.append(float(input("Enter speed: ")))
    time.append(float(input("Enter time: ")))
X, Y = np.meshgrid(speed, time)
Z = X * Y
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z)
ax.set_xlabel("Speed")
ax.set_ylabel("Time")
ax.set_zlabel("Distance")
plt.show()
