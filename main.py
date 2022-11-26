from menu import menu
from fileHandling import *
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
        filedelete()
        csoportszám = 0
        while csoportszám != len(teams)/4:
            groupwinner(csoportszám)
            csoportszám+=1
        nyolcaddonto = nyolcad()
        groups(nyolcaddonto,int(len(nyolcaddonto)/4))
        szimulator()
        filedelete()
        nyolcaddontocsoportszam =0
        while nyolcaddontocsoportszam != len(nyolcaddonto)/4:
            groupwinner(nyolcaddontocsoportszam)
            nyolcaddontocsoportszam+=1

            


