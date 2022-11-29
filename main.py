from menu import *
from fileHandling import *
from randomgroups import groups
from simulate import *
from search import *
golperteamFileDelete()
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
        goalcounter()
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
                y = -1
                while y !=0:
                    y = choice2submenu()
                    if y == 0:
                        pass   
                    elif y == 1:
                        legfiatalabb()
                    elif y == 2:
                        Legidosebb()
                    elif y == 3:
                        kor()
                    elif y == 4:
                        inbetween()
            elif x == 5:
                z = -1
                while z !=0:
                    z = choice2submenu2()
                    if z ==0:
                        pass
                    elif z ==1:
                        poz("Védő")
                    elif z ==2:
                        poz("Középpályás")
                    elif z ==3:
                        poz("Csatár")
                    elif z ==4:
                        poz("Edző")
                
            
        

            


