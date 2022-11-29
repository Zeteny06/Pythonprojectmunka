def Csapatok():
    teams = []
    f = open("Játékosok.csv","r",encoding="utf8")
    f.readline()
    for row in f:
        splitted = row.split(";")
        x = splitted[4]
        y = x.strip()
        if y not in teams:
            teams.append(y) 
    f.close()
    return teams
def nyolcad():
    nyolcad = []
    f = open("csoportnyertes.csv","r",encoding="UTF8")
    for row in f:
        x = row.strip("\n")
        nyolcad.append(x)
    return nyolcad

def golperteamFileDelete():
    f= open("GOL.csv","w",encoding="UTF8")
    f.close()

    