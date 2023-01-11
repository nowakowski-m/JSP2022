import time
import os
from os import path
import glob

foldername = str(input("Wprowadz nazwe folderu do odczytu: "))
path = glob.glob(foldername + "/plik_zaszyfrowany*.txt")
path_list = (path[0]).split("_")
shift = path_list[(len(path_list)-2)]
shift = int(shift)

load_file = open(path[0], "r") 
hackedText = load_file.read()
load_file.close()

alph_k_v = {
'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
}

alph_v_k = {
1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h',
9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n',
15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t',
21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'
}

encryptedText = ""

for x in range (len(hackedText)):

    isUpperCase = False

    if (hackedText[x]).isupper() == True:
        isUpperCase = True

    else:
        pass

    tempLetter = hackedText[x].lower()

    if tempLetter in alph_k_v.keys():
        x_position = alph_k_v.get(tempLetter)

        if x_position - shift < 1:
            x_position = 26 + (x_position - shift)
        
        else:
            x_position = x_position - shift

        if isUpperCase == True:
            encryptedText += (alph_v_k.get(x_position)).upper()
        
        if isUpperCase == False:
            encryptedText += alph_v_k.get(x_position)
    
    else:

        if isUpperCase == True:
            encryptedText += tempLetter.upper()
        
        if isUpperCase == False:
            encryptedText += tempLetter

timestr = time.strftime("%Y%m%d")

save_file = open(foldername + "/plik_deszyfrowany_" + (str(shift)) + "_" + timestr + ".txt", 'w')
save_file.write(encryptedText)
save_file.close()