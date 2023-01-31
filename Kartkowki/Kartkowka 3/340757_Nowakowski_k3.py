# Napisz funkcję która bierze sekwencję z DNA,
# np. s = "GTACAGTA"
# zamienia literki:
# A - > T, C -> G, T -> A, G -> C,
# i calosc odwraca. 
# Jesli jakas literka nie zawiera sie w kluczach,
# zwrocic pusty napis i wyswietlic wiadomosc.

def dnaChange(sekw:str) -> str:
    sekwKey = {
        "A": "T",
        "C": "G",
        "T": "A",
        "G": "C"
    }

    sekwList = list(sekw)

    for x in range (0, len(sekw)):
        if sekwList[x] in sekwKey.keys():
            sekwList[x] = sekwKey.get(sekwList[x])
        else:
            return ("")
    sekwFinal = "".join(sekwList)
    return sekwFinal[::-1]


sekw = str(input("Wprowadz sekwencje: "))
print(dnaChange(sekw))

if dnaChange(sekw) == "":
    print("Błędna sekwencja.")