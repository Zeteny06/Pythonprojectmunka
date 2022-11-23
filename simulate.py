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
    f = open("Pythonprojectmunka\csoportok.csv","r",encoding="UTF8")
    csapatfile = open("Pythonprojectmunka\eredmenyek.csv","w",encoding="UTF8")
    for index, group in enumerate(f):
        splitted = group.strip().split(";")
        for csapat1 in splitted:
            for csapat2 in splitted:
                if csapat1 != csapat2:
                    hazai = gol()
                    vendeg = gol()
                    # if hazai > vendeg:
                    #     nyert.append(csapat1)
                    # elif hazai < vendeg:
                    #     nyert.append(csapat2)
                    # else:
                    #     nyert.append(csapat1,csapat2)
                    csapatfile.write(f"{index};{hazai};{vendeg};{csapat1};{csapat2}\n")
    csapatfile.close()
    f.close()
