n = int(input("Enter number of people: "))
doctor = []
professor = []
singer = []
actor = []
for i in range(n):
    name = input("Enter name: ")
    occupation = input("Enter occupation: ")
    if occupation == "Doctor":
        doctor.append(name)
    elif occupation == "Professor":
        professor.append(name)
    elif occupation == "Singer":
        singer.append(name)
    elif occupation == "Actor":
        actor.append(name)
doctor.sort()
professor.sort()
singer.sort()
actor.sort()
m = max(len(doctor), len(professor), len(singer), len(actor))
for i in range(m):
    d = doctor[i] if i < len(doctor) else "NULL"
    p = professor[i] if i < len(professor) else "NULL"
    s = singer[i] if i < len(singer) else "NULL"
    a = actor[i] if i < len(actor) else "NULL"
    print(d, p, s, a)
