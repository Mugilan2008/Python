num = float(input("Enter a number to take square root: "))
power = int(input("Enter the power value for the number: "))
square_root = lambda x: x**0.5
power_value = lambda x, y: x ** y
print("Square Root =", square_root(num))
print("Power =", power_value(num, power))
