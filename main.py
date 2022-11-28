from menu import *
from fileHandling import *
from randomgroups import groups
from simulate import *
from search import *

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
        donto = nyolcad()
        groups(donto,1)
        szimulator()
        filedelete()
        groupwinner(0)
    elif choice == 2:
        x = -1
        while x != 0:
            x = choice2()
            if x == 0:
                pass   
            elif x == 1:
                jatekos()
            elif x == 2:
                csapat()
            elif x == 3:
                mezszam()
            elif x == 4:
                kor()
            elif x == 5:
                poz()
            
        

            


