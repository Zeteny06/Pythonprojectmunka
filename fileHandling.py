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
