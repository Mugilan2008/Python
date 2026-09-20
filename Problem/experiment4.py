input_power = float(input("Enter Input Power (W): "))
output_power = float(input("Enter Output Power (W): "))
efficiency = lambda op, ip: (op / ip) * 100
print("Efficiency = ",efficiency(output_power, input_power))
