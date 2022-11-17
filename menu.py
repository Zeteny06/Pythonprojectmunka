def menu():
    option = -1
    while option < 0 or option > 5:
        print("0-kilépés")
        print("1-Random csoport készítés")
        print("2-Keresés")
        print("3-új")
        print("4-törlés")
        print("5-Módosítás")
        option = int(input("Válasszon a fentiek közül:"))
    return option