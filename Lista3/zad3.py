print ("Program obliczy wszystkie pierwiastki rzeczywiste dla równania kwadratowego o postaci ax^2 + bx + c = 0")

a = float(input ("Podaj współczynnik a: "))
b = float(input ("Podaj współczynnik b: "))
c = float(input ("Podaj współczynnik c: "))

if (a!=0):
    delta = b**2 - (4*a*c)

    if (delta > 0):
        x1 = ((-b)-(delta**(1/2)))/(2*a)
        x2 = ((-b)+(delta**(1/2)))/(2*a)
        print ("Równanie ma dwa pierwiastki: ", x1, x2)
    if (delta == 0 ):
        x1 = (-b)/(2*a)
        print ("Równanie ma jeden pierwiastek: ", x1)
    if (delta < 0 ):
        print ("Równanie nie ma pierwiastków, delta < 0.")
else:
    print("Wprowadzone równanie nie jest kwadratowe!")