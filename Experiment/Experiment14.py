import matplotlib.pyplot as plt
import numpy as np
n = int(input("Enter number of speed values: "))
speed = []
distance = []
time = float(input("Enter time: "))
for i in range(n):
    s = float(input("Enter speed: "))
    speed.append(s)
    distance.append(s * time)
x = np.array(speed)
y = np.array([time])
z = np.array([distance])
X, Y = np.meshgrid(x, y)
Z = np.array([distance])
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z)
ax.set_xlabel("Speed")
ax.set_ylabel("Time")
ax.set_zlabel("Distance")
plt.show()
