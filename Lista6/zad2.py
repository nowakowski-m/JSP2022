import SzyfrCezara as sc
import os

os.system("clear")

tekstInput = str(input("Wprowadz tekst: "))

finalSzyfred = sc.szyfrCezara(tekstInput)

finalOdszyfred = sc.odszyfrCezara(finalSzyfred, tekstInput)

print ("\nZaszyfrowany: " + finalSzyfred + "\n")
print ("Odszyfrowany: " + finalOdszyfred + "\n")