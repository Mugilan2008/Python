import matplotlib.pyplot as plt
n = int(input("Enter number of product categories: "))
names = []
sales = []
for i in range(n):
    name = input("Enter product category: ")
    value = float(input("Enter sales: "))
    names.append(name)
    sales.append(value)
plt.pie(sales, labels=names, autopct="%1.1f%%")
plt.title("Product Sales")
plt.show()
