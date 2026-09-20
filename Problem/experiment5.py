ratings = []
n = int(input("Enter how many transformer ratings: "))
for i in range(n):
    rating = int(input("Enter transformer rating: "))
    ratings.append(rating)
capacity = int(input("Enter maximum capacity: "))
result = []
for i in ratings:
    if i > capacity:
        result.append(i)
print("Given transformer ratings:",ratings)      
print("Transformers greater than capacity:", result)
