# Zadanie 5

samo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Funkcja sprawdzająca punktacje dla pojedynczego słowa.

def SingleWord(single:str) -> str:
    
    pkt = 0
    amountOfSamo = 0
    
    for ele in range (len(single)):

        if single[ele] in samo:
            amountOfSamo += 1
            if amountOfSamo % 2 == 0:
                pkt = 2
            else:
                pkt = 1

    return pkt

# Funkcja sprawdzająca punktacje dla więcej niż jednego słowa w tekście.

def wholeText(text:str) -> str:
    
    finalPkt = 0

    listOfText = text.split(' ')

    for element in listOfText:
        finalPkt += SingleWord(element)

    return finalPkt

# Funkcja pobierająca tekst od użytkownika, zwraca punkty.

def TextInput():

    entered = str(input("Podaj tekst: "))

    numOfElements = entered.split(' ')

    if (len(numOfElements)) == 1:

        return SingleWord(entered)

    else:

        return wholeText(entered)

# Użycie funkcji

print(TextInput())