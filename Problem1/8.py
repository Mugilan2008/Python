import numpy as np
numbers = input("Enter numbers: ").split()
arr = np.array(numbers, dtype=float)
print("Reversed array:")
print(arr[::-1])
