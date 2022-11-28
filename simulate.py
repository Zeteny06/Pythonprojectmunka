from random import randint

def gol():
    esely = randint(1,5)
    if esely == 1:
        return 1
    elif esely == 2:
        return 2
    elif esely == 3:
        return 3
    elif esely == 4:
        return 4
    elif esely == 5:
        return 5


def szimulator():
    f = open("csoportok.csv","r",encoding="UTF8")
    csapatfile = open("eredmenyek.csv","w",encoding="UTF8")
    for index, group in enumerate(f):
        splitted = group.strip().split(";")
        for csapat1 in splitted:
            for csapat2 in splitted:
                if csapat1 != csapat2:
                    hazai = gol()
                    vendeg = gol()
                    csapatfile.write(f"{index};{hazai};{vendeg};{csapat1};{csapat2}\n")
    csapatfile.close()
    f.close()

def groupwinner(csoportszám):
    f = open("eredmenyek.csv","r",encoding="UTF8")
    csoportnyertes = open("csoportnyertes.csv","a",encoding="UTF8")
    csapatok =[]
    pontok = {

    }
    for row in f:
        splitteddata = row.strip().split(";")
        if int(splitteddata[0]) ==csoportszám: 
            if splitteddata[3] not in csapatok:
                csapatok.append(splitteddata[3])
    f.close()
    f = open("eredmenyek.csv","r",encoding="UTF8")
    for x in csapatok:
        pontok.update({x:0})
    for row in f:
        splitteddata = row.strip().split(";")  
        if int(splitteddata[0]) == csoportszám:
            if int(splitteddata[1]) > int(splitteddata[2]):
                pontok[splitteddata[3]] += 3
            elif int(splitteddata[1]) < int(splitteddata[2]):
                pontok[splitteddata[4]] += 3
            elif int(splitteddata[1]) == int(splitteddata[2]):
                pontok[splitteddata[3]] += 1
                pontok[splitteddata[4]] += 1
        
    print(pontok)
    pont = 0
    csapat =[]
    for key,value in pontok.items():
        if value > pont:
            pont = value
            csapat.clear()
            
        if value == pont:
            csapat.append(key)
    csoportnyertes.writelines(f"{csapat[0]}\n")


        
    f.close()
    csoportnyertes.close()

def filedelete():
    csoportnyertes = open("csoportnyertes.csv","w",encoding="UTF8")
    csoportnyertes.close()



