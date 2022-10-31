import re, os

os.system("cls")
haslo = input("Wprowadź hasło: ")
print("\n")

dlugosc = len(haslo)

male = re.compile('[a-z]+')
duze = re.compile('[A-Z]+')
liczby = re.compile('[0-9]+')
znaki = re.compile('["$","#","@"]')

m = male.search(haslo)
d = duze.search(haslo)
l = liczby.search(haslo)
z = znaki.search(haslo)

if 6 <= dlugosc <= 16:

    if (m and d and l and z):
        print ("Podane hasło jest prawidłowe.")
    
    if m:
        pass
    else:
        print ("Brak małej litery.")
    if d:
        pass
    else:
        print ("Brak wielkiej litery.")
    if l:
        pass
    else:
        print ("Brak liczby.")
    if z:
        pass
    else:
        print ("Brak wymaganych znaków.")

if dlugosc < 6:
    print("Podane hasło jest za krótkie.")
if dlugosc > 16:
    print("Podane hasło jest za długie.")

print ("\n")