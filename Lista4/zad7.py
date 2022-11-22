import math

silnia = math.factorial

x = int(input("Podaj liczbę n wierszy trójkąta Pascala: "))

print( (int(x/2)+2) * " ",  "1", end = '')

for n in range (1, x+1):
    if n % 2 == 0:
        print ("\n", (int(((x-n)+1)/2))*" ", end = '')
    else:
        print ("\n", (int(((x-n)+2)/2))*" ", end = '')
    for k in range (0, n+1):
        print (int ( silnia(n) / silnia(k) / silnia(n-k) ) , end = ' ')