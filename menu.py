def menu():
    option = -1
    while option < 0 or option > 3:
        print("0-kilépés")
        print("1-Random csoport készítés")
        print("2-Keresés")
        print("3-Szimulálás")
        option = int(input("Válasszon a fentiek közül:"))
    return option