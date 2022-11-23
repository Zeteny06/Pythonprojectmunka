from menu import menu
from fileHandling import Csapatok
from randomgroups import groups
from simulate import *

choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        teams =Csapatok()
        groups(teams,int(len(teams)/4))
        print(len(teams))
        szimulator()


