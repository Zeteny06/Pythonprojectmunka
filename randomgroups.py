import random

def groups(csapatok, Csoportszam):
    random.shuffle(csapatok)
    print(Csoportszam)
    all_groups = []
    for index in range(Csoportszam):
        group = csapatok[index::Csoportszam]
        all_groups.append(group)
    print(all_groups)
    for index, group in enumerate(all_groups):
        print(f"Csoport {index+1}: {' / '.join(group)}\n")
    f = open("csoportok.csv","w",encoding="UTF8")
    for row in all_groups:
        y = ""
        for x in row:
            y += x + ";"
        f.writelines(y.strip(";")+"\n")
    return all_groups