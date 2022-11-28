def menu():
    option = -1
    while option < 0 or option > 3:
        print("0-kilépés")
        print("1-Random csoport készítés")
        print("2-Keresés")
        print("3-Szimulálás")
        option = int(input("Válasszon a fentiek közül:"))
    return option
def choice2():
    option = -1
    while option < 0 or option > 5:
        print("0.Vissza\n1.Játékos\n2.Csapat\n3.Mezszám\n4.Kor\n5.Pozíció")
        option =int(input("Válassz: "))
    return option
def choice2submenu():
    option = -1
    while option < 0 or option > 4:
        print("0.Vissza\n1.Legfiatalabbak\n2.Legidősebb\n3.Pontos keresés\n4.Két életkor között")
        option =int(input("Válassz: "))
    return option