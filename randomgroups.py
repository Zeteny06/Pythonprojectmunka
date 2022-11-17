import random

def groups(csapatok, Csoportszam):
    random.shuffle(csapatok)
    print(Csoportszam)
    all_groups = []
    for index in range(Csoportszam):
        group = csapatok[index::Csoportszam]
        all_groups.append(group)
    f = open("Pythonprojectmunka\Pythonprojectmunka\groups.csv","w",encoding="UTF8")
    for index, group in enumerate(all_groups):
        f.writelines(f"Csoport {index+1}: {' / '.join(group)}\n")
        # print(f"Csoport {index+1}: {' / '.join(group)}\n")
        f.close()
    return all_groups