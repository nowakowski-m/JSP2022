n = int(input("Podaj liczbe calkowita n pierwszych elementow szeregu harmonicznego: "))

while n <= 0:
    print("Zla wartosc, podaj liczbe calkowita n wieksza od 0.")
    n = int(input("Podaj liczbe n pierwszych elementow szeregu harmonicznego: "))

z = 1

for x in range (2, n+1):
    z += ( 1/x )

print ("\nSuma n elementow: ", z)