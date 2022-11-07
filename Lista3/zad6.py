i = int(input("Podaj liczbę kolumn. "))
j = list(range(1,11))

x = 1
while x <= i:
    y = 0
    for el in j:
        z = el*x
        print (z, end="\t")
    x += 1
    print ("")
    