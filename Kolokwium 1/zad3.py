# Zadanie 3

import math as m

def metersCircleField(r, unit):
    if unit == 'mm':
        r = r*0.001
        f = m.pi*r*r
        return f
    if unit == 'cm':
        r = r*0.01
        f = m.pi*r*r
        return f
    if unit == 'm':
        f = m.pi*r*r
        return f

# Przykładowe użycie

print ( metersCircleField (5, 'mm'), "m^2" )