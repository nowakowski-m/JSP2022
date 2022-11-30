import math

lista = []
for i in range (1, 11):
    lista.append(i)

x = int(input("Otrzymaj: 1. Sume, 2. Iloczyn: "))
print()

while x:
    if x == 1:
        suma = sum(lista)
        print("Suma: ", suma, "\n")
        break
    if x == 2: 
        iloczyn = math.prod(lista)
        print("Iloczyn: ", iloczyn, "\n")
        break
    if x != 1 or x != 2:
        print("Niepoprawna wartość.\n")
        x = int(input("Otrzymaj: 1. Sume, 2. Iloczyn: \n"))
        print()

    