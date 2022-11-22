z1 = int(input("Podaj pierwsza liczbe calkowita: "))
z2 = int(input("Podaj druga liczbe calkowita: "))

if z1 > z2:
    for dzielnik in range (z1, 0, -1):
        if z1 % dzielnik == 0 and z2 % dzielnik == 0:
            print ("\nNajwiekszy wspolny dzielnik obu liczb to: ", dzielnik)
            break
    
if z1 < z2:
    for dzielnik in range (z2, 0, -1):
        if z1 % dzielnik == 0 and z2 % dzielnik == 0:
            print ("\nNajwiekszy wspolny dzielnik obu liczb to: ", dzielnik)
            break

if z1== z2:
    for dzielnik in range (z1, 0, -1):
        if z1 % dzielnik == 0 and z2 % dzielnik == 0:
            print ("\nNajwiekszy wspolny dzielnik obu liczb to: ", dzielnik)
            break