def obwod(x: float, y: float, z: float) -> float:
    obw = x + y + z
    return obw

def pole(x: float, y: float, z: float) -> float:
    p = 0.5 * ( x + y + z)
    return p
    
def boki(x: float, y:float, z: float) -> str:
    if x == y == z:
        bok = "Równoboczny"
    elif x == y != z or x != y == z or x != z == y or x == z != y:
        bok = "Równoramienny"
    elif x != y != z or x != z != y:
        bok = "Różnoboczny"
    return bok

def katy(x: float, y:float, z: float) -> str:
    if ( x*x == ( y*y + z*z ) ) or ( y*y == x*x + z*z ) or ( z*z == x*x + y*y):
        kat = "Prostokątny"
    if ( x*x < ( y*y + z*z ) ) or ( y*y < x*x + z*z ) or ( z*z < x*x + y*y):
        kat = "Rozwartokątny"
    if ( x*x == ( y*y + z*z ) ) or ( y*y == x*x + z*z ) or ( z*z == x*x + y*y):
        kat = "Ostrokątny"
    return kat