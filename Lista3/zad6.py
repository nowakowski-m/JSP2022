i = int(input("Podaj liczbę wierszy: "))
y = list(range(0,(i+1)))
j = list(range(1,11))

for k in range(len(j)):    
    for x in range(len(y)):
        z = x*j[k]
        z