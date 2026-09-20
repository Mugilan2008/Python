m = int(input("Enter number of houses: "))
houses = []
for i in range(m):
    area, price = map(int, input("Enter house area and price: ").split())
    houses.append((area, price))
n = int(input("Enter number of clients: "))
clients = []
for i in range(n):
    area, price = map(int, input("Enter client area and maximum price: ").split())
    clients.append((area, price))
used = [False] * m
def match(client, visited):
    a, p = client
    for i in range(m):
        house_area, house_price = houses[i]
        if not visited[i] and not used[i]:
            if house_area > a and house_price <= p:
                visited[i] = True
                if not used[i]:
                    used[i] = True
                    return True
    return False
count = 0
for client in clients:
    visited = [False] * m
    if match(client, visited):
        count += 1
print("Maximum houses sold =", count)
