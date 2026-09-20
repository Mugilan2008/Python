h = int(input("Enter height of board: "))
w = int(input("Enter width of board: "))
a = []
for i in range(h):
    row = list(map(int, input("Enter row: ").split()))
    a.append(row)
area = 0
for i in range(h):
    for j in range(w):
        if a[i][j] > 0:
            area += 2
        if i == 0:
            area += a[i][j]
        else:
            area += max(0, a[i][j] - a[i-1][j])
        if i == h - 1:
            area += a[i][j]
        if j == 0:
            area += a[i][j]
        else:
            area += max(0, a[i][j] - a[i][j-1])
        if j == w - 1:
            area += a[i][j]
print("Surface Area =", area)
