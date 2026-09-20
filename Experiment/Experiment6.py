class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
    def display_battery_status(self):
        print(f"Phone: {self.brand} {self.model}")
        print(f"Battery Status: {self.battery_percentage}%")
brand = input("Enter Mobile Brand: ")
model = input("Enter Mobile Model: ")
battery = float(input("Enter Battery Percentage: "))
phone = MobilePhone(brand, model, battery)
phone.display_battery_status()
