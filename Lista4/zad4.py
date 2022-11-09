print("Program zwróci n-ty element ciągu geometrycznego.")

n = int(input("Podaj numer elementu ciągu: "))
a1 = int(input("Podaj wartość pierwszego elementu ciągu: "))
q = int(input("Podaj wartość iloczynu ciągu: "))

an = a1*(q**(n-1))
print (an)