import matplotlib.pyplot as plt
python = float(input("Enter Python percentage: "))
java = float(input("Enter Java percentage: "))
cpp = float(input("Enter C++ percentage: "))
javascript = float(input("Enter JavaScript percentage: "))
languages = ["Python", "Java", "C++", "JavaScript"]
values = [python, java, cpp, javascript]
plt.pie(values, labels=languages, autopct="%1.1f%%")
plt.title("Favourite Programming Languages")
plt.show()
