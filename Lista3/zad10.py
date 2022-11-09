parzyste = []
for x in range (100,401):
    wszystkie = list(map(int, str(x)))
    if wszystkie[0]%2==0 and wszystkie[1]%2==0 and wszystkie[2]%2==0:
        parzyste.append(x)
print (parzyste)