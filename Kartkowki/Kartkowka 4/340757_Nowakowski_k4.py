import os
import time

os.system("clear")

start_execute_time = time.perf_counter()

load_file = open("payload_340757.txt", "r") 
encryptedText = load_file.read()
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

shift = 16
hackedText = ""

for x in range (len(encryptedText)):

    isUpperCase = False

    if (encryptedText[x]).isupper() == True:
        isUpperCase = True

    else:
        pass

    tempLetter = encryptedText[x].lower()

    if tempLetter in alph_k_v.keys():
        x_position = alph_k_v.get(tempLetter)

        if x_position + shift > 26:
            x_position = x_position + shift - 26
        
        else:
            x_position = x_position + shift

        if isUpperCase == True:
            hackedText += (alph_v_k.get(x_position)).upper()
        
        if isUpperCase == False:
            hackedText += alph_v_k.get(x_position)
    
    else:

        if isUpperCase == True:
            hackedText += tempLetter.upper()
        
        if isUpperCase == False:
            hackedText += tempLetter


save_file = open("hacked_340757.txt", 'w', encoding='utf-8')
save_file.write(hackedText)
save_file.close()

print(hackedText)

if "Michał" in hackedText and "Nowakowski" in hackedText and "340757" in hackedText:
    print("\n\x1b[42mOdszyfrowano pomyślnie!\x1b[0m\n")

finish_execute_time = time.perf_counter() - start_execute_time
print("Czas działania: \x1b[32m" + str(finish_execute_time) + "\x1b[0m")