lst = []
n = int(input("Enter number of commands: "))
for _ in range(n):
    command = input().split()
    match command[0]:
        case "insert":
            lst.insert(int(command[1]), int(command[2]))
        case "print":
            print(lst)
        case "remove":
            lst.remove(int(command[1]))
        case "append":
            lst.append(int(command[1]))
        case "sort":
            lst.sort()
        case "pop":
            lst.pop()
        case "reverse":
            lst.reverse()
