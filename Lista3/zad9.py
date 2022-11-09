m = int(input("Podaj ilość wierszy (m ): "))
n = int(input("Podaj ilość kolumn (n ): "))

for x in range(1, m+1):
    for y in range (1, n+1):
        print(x*y, end="\t") 
    print()