choice = int(input("Choose:\n1. Voltage Source to Current Source\n2. Current Source to Voltage Source\nEnter choice: "))
if choice == 1:
    V = float(input("Enter Voltage (V): "))
    R = float(input("Enter Series Resistance (Ohms): "))
    I = V / R
    print("\nEquivalent Current Source")
    print("Current =", round(I, 2), "A")
    print("Parallel Resistance =", R, "Ohms")
elif choice == 2:
    I = float(input("Enter Current (A): "))
    R = float(input("Enter Parallel Resistance (Ohms): "))
    V = I * R
    print("\nEquivalent Voltage Source")
    print("Voltage =", round(V, 2), "V")
    print("Series Resistance =", R, "Ohms")
else:
    print("Invalid Choice")
