n = int(input("Podaj liczbe calkowita dodatnia n, dla ktorej program obliczy silnie: "))

while n <= 0:
    print("Zla liczba, sprobuj ponownie.")
    n = int(input("Podaj liczbe calkowita dodatnia n, dla ktorej program obliczy silnie: "))

silnia = 1

for x in range (1, n+1):
    silnia *= x

print (silnia)