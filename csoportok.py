import random
from fileHandling import *


def make_random_groups(csapatok, csoportdb):
    random.shuffle(csapatok)
    all_groups = []
    for index in range(csoportdb):
        group = csapatok[index::csoportdb]
        all_groups.append(group)
    for index, group in enumerate(all_groups):
        print(f"csoport {index+1}: {' / '.join(group)}\n")