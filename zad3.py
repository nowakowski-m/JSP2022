import math

def rad_Deg():
    rad = float(input("Podaj kat w radianach: "))
    deg = (180/math.pi)*rad
    print ("ans = ", deg,"°")

def deg_Rad():
    deg = float(input("Podaj kat w stopniach: "))
    rad = (deg*math.pi)/180
    print ("ans = ", rad, "rad")

x = int(input("1. Przelicz radiany na stopnie.\n2. Przelicz stopnie na radiany.\n*  Wybierz rodzaj funkcji: "))

while x:
    if x == 1:
        rad_Deg()
        break
    if x == 2: 
        deg_Rad()
        break
    if x != 1 or x != 2:
        print("Niepoprawna wartość.")
        x = int(input("1. Przelicz radiany na stopnie.\n2. Przelicz stopnie na radiany.\n*  Wybierz rodzaj funkcji: "))
        print()