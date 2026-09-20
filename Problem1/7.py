import math
import numpy as np
A = np.array(list(map(float, input("Enter A: ").split())))
B = np.array(list(map(float, input("Enter B: ").split())))
C = np.array(list(map(float, input("Enter C: ").split())))
D = np.array(list(map(float, input("Enter D: ").split())))
AB = B - A
BC = C - B
CD = D - C
X = np.cross(AB, BC)
Y = np.cross(BC, CD)
cos_phi = np.dot(X, Y) / (np.linalg.norm(X) * np.linalg.norm(Y))
phi = math.degrees(math.acos(cos_phi))
print("Angle =", round(phi, 2))
