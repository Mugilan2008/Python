import matplotlib.pyplot as plt
n = int(input("Enter number of readings: "))
time = []
calories = []
for i in range(n):
    t = float(input("Enter exercise time: "))
    c = float(input("Enter calories burned: "))
    time.append(t)
    calories.append(c)
plt.scatter(time, calories)
plt.xlabel("Exercise Time")
plt.ylabel("Calories Burned")
plt.title("Exercise Time vs Calories")
plt.show()
