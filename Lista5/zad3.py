def rome_to_arabian(romeNum:str) -> int:
    romeStr = str(romeNum)

    calc = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    arabianNum = 0
    v = 0
    x = 0

    for romeChars in range (0, len(romeStr)):
        if romeStr[romeChars] in calc.keys():
            arabianNum += calc[romeStr[romeChars]]
            romeChars+=1

    for iv in range(0, (len(romeStr)-1)):
        if "I" in romeStr[iv] and "V" in romeStr[iv+1]:
            v+=1

    for ix in range(0, (len(romeStr)-1)):
        if "I" in romeStr[ix] and "X" in romeStr[ix+1]:
            x+=1

    #Właściwie to te fory chyba nie są do końca potrzebne i starczyły by ify,
    #bo w zapisie liczby rzymskiej chyba nie może pojawić się kilka razy "IV" lub "IX".

    finalNum = arabianNum - v*6 + v*4 - x*11 + x*9

    return finalNum

romeNum = input("Wprowadź liczbę rzymską: ")
print (rome_to_arabian(romeNum) )