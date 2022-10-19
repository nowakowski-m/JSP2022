import math

print ("Podaj dlugosc boku a")
a = int(input())
print ("Podaj dlugosc boku b") 
b = int(input())
print ("Podaj wartosc kata miedzy nimi")
x = int(input())

print (0.5*a*b*math.sin(x*math.pi/180))
