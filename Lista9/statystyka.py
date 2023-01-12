import numpy as np
import sys
import os

if len(sys.argv) == 1:
    dane = [int(line) for line in sys.stdin]
else:
    dane = [int(args) for args in sys.argv[1:]]

avg = np.average(dane)
var = np.var(dane)
dev = np.std(dane)

os.system("clear")
print("Podane wartosci:")
print(dane)
print("\n" + "Srednia = " + str(avg) + "\n" + "Wariancja = " + str(var) + "\n" + "Odchylenie standardowe = " + str(dev))