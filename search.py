def jatekos():
    nevek = []
    jatekosnev = input("Add meg a nevét:")
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    for row in f:
        data = row.strip().split(";")
        if jatekosnev.upper() in data[0].upper() :
            nevek.append(data[0])
    for nev in nevek:
        print(f"\t{nev}")

def csapat():
    csapatok = []
    csapatnev = input("Add meg a nevét:")
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    for row in f:
        data = row.strip().split(";")
        if csapatnev.upper() in data[4].upper() :
            if data[4]not in csapatok:
                csapatok.append(data[4])
    for csapat in csapatok:
        print(f"\t{csapat}")
def mezszam():
    people = []
    mezszam = int(input("Add meg a mezszámát:"))
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    for row in f:
        data = row.strip().split(";")
        if data[1] != "-":
            if int(data[1]) == mezszam :
                people.append(data[0])
    for person in people:
        print(f"\t{person}")
def kor():
    pass
def poz():
    pass