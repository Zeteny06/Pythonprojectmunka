import random

def groups(csapatok, Csoportszam):
    random.shuffle(csapatok)
    print(Csoportszam)
    all_groups = []
    for index in range(Csoportszam):
        group = csapatok[index::Csoportszam]
        all_groups.append(group)
    for index, group in enumerate(all_groups):
        print(f"Csoport {index+1}: {' / '.join(group)}\n")
    return all_groups