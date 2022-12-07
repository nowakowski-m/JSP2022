import trojkat as t
import os

os.system("clear")
x = float(input("Podaj 1 bok: "))
y = float(input("Podaj 2 bok: "))
z = float(input("Podaj 3 bok: "))
print("")

if x+y > z or y+z > x or x+z > y:
    print("Obwód:", (t.obwod(x, y, z)))
    print("Pole:", (t.pole(x, y, z)))
    print(t.boki(x, y, z))
    print(t.katy(x, y, z))
    print("")
else:
    print("Podane długości nie spełniają warunków istnienia trójkąta.")
    print("")