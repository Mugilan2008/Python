import numpy as np
elements = list(map(float, input("Enter space-separated numbers: ").split()))
arr = np.array(elements)
product_val = np.prod(arr)
sum_val = np.sum(arr)
print("Product:", product_val)
print("Sum:", sum_val)
if product_val > sum_val:
    print("Result: Product is greater than Sum")
elif product_val < sum_val:
    print("Result: Sum is greater than Product")
else:
    print("Result: Product and Sum are equal")
