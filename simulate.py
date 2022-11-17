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


def szimulator(allgroup):
    for group in allgroup:
        x = group
        splitted = x.split("/")
        for x in splitted:
            for y in splitted:
                nyert= []
                if splitted[x] == splitted[y]:
                    pass
                else:
                    hazai = gol()
                    vendeg = gol()
                    if hazai > vendeg:
                        nyert.append[x]
                    elif hazai < vendeg:
                        nyert.append[y]
                    else:
                        nyert.append[x,y]
    print(nyert)