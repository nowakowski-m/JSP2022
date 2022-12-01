def szyfr(text_inputed: str) -> str:

    textKey = {
        "a" : "y",
        "e" : "i",
        "i" : "o",
        "o" : "a",
        "y" : "e"
    }

    textList = list(textStr)
    textLen = len(textStr)

    for x in range (0, textLen):
        if textList[x] in textKey.keys():
            textList[x] = textKey.get(textList[x])

    textSzyfred = "".join(textList)
    return textSzyfred

def odszyfr(szyfr):

    textKey = {
        "y" : "a",
        "i" : "e",
        "o" : "i",
        "a" : "o",
        "e" : "y"
    }

    textList = list(szyfr)
    textLen = len(szyfr)

    for x in range (0, textLen):
        if textList[x] != textStr[x]:
            if textList[x] in textKey.keys():
                textList[x] = textKey.get(textList[x])

    textOdszyfred = "".join(textList)
    return textOdszyfred



textStr = str(input("Wprowadź tekst do zaszyfrowania: "))
res = szyfr(textStr)
print(f"Zaszyfrowany: {res}")
print("Odszyfrowany:", odszyfr(res))