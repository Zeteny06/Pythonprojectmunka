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
    people = []
    kor = int(input("Add meg az életkort:"))
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    for row in f:
        data = row.strip().split(";")
        if int(data[2]) == kor :
            people.append(data[0])
    for person in people:
        print(f"\t{person}")
def legfiatalabb():
    people = []
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    compareable = 9999
    for row in f:
        data = row.strip().split(";")
        if int(data[2]) == compareable:
            people.append(data[0])
        elif int(data[2]) < compareable :
            people.clear()
            people.append(data[0])
            compareable = int(data[2])
    for person in people:
        print(f"\t{person}:{compareable}")
def Legidosebb():
    people = []
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    compareable = -1
    for row in f:
        data = row.strip().split(";")
        if data[3]!= "Edző":
            if int(data[2]) == compareable:
                people.append(data[0])
            elif int(data[2]) > compareable :
                people.clear()
                people.append(data[0])
                compareable = int(data[2])
            else:
                pass
    for person in people:
        print(f"\t{person}:{compareable}")
def inbetween():
    kezdes = int(input("Add meg a minimum életkort:"))
    befejezes = int(input("Add meg a maximum életkort:"))
    people = []
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    for row in f:
        data = row.strip().split(";")
        if int(data[2]) >= kezdes and int(data[2]) <= befejezes:
            people.append(data[0])
    for person in people:
        print(f"\t{person}")
def poz(position):
    people = []
    f = open("Játékosok.csv","r",encoding="UTF8")
    f.readline()
    for row in f:
        data = row.strip().split(";")
        if data[3] == position:
            people.append(data[0])
    for person in people:
        print(f"\t{person}")
