alph_k_v = {
'a':1, 'ą':2, 'b':3, 'c':4, 'ć':5, 'd':6, 'e':7, 'ę':8, 'f':9,
'g':10, 'h':11, 'i':12, 'j':13, 'k':14, 'l':15, 'ł':16, 'm':17,
'n':18, 'o':19, 'p':20, 'q':21, 'r':22, 's':23, 'ś':24, 't':25,
'u':26, 'v':27, 'w':28, 'x':29, 'y':30, 'z':31, 'ź':32, 'ż':33
}

alph_v_k = {
1:'a', 2:'ą', 3:'b', 4:'c', 5:'ć', 6:'d', 7:'e', 8:'ę', 9:'f',
10:'g', 11:'h', 12:'i', 13:'j', 14:'k', 15:'l', 16:'ł', 17:'m',
18:'n', 19:'o', 20:'p', 21:'q', 22:'r', 23:'s', 24:'ś', 25:'t',
26:'u', 27:'v', 28:'w', 29:'x', 30:'y', 31:'z', 32:'ź', 33:'ż'
}

def szyfrCezara (tekstInput: str) -> str:

    tekst = tekstInput.lower()
    szyfrTekstList = []

    for x in range (0, len(tekst)):
        for y in range (0, len(alph_k_v)+1):
            if alph_k_v.get(tekst[x]) == y:
                if y + (ord(tekst[x])) > (len(alph_k_v)):
                    y = (y+(ord(tekst[x]))) % (len(alph_k_v))
                else:
                    y = y + (ord(tekst[x]))
                szyfrTekstList.append(alph_v_k.get(y))
                break
            elif y == 32:
                szyfrTekstList.append(tekst[x])

    szyfrTekst = ''.join(szyfrTekstList)

    return szyfrTekst

def odszyfrCezara (szyfrTekst, tekst: str) -> str:
    odszyfredTekstList = []
    for x in range (0, len(szyfrTekst)):
        for y in range (0, len(alph_k_v)+1):
            if alph_k_v.get(szyfrTekst[x]) == y:
                if y - (ord(szyfrTekst[x])) < (len(alph_k_v)):
                    y = (y-(ord(tekst[x]))) % (len(alph_k_v))
                else:
                    y = y - (ord(szyfrTekst[x]))
                odszyfredTekstList.append(alph_v_k.get(y))
                break
            elif y == 32:
                odszyfredTekstList.append(szyfrTekst[x])

    odszyfredTekst = ''.join(odszyfredTekstList)

    return odszyfredTekst