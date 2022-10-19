import cmath
print ("Podaj liczbe zespolona, np. 5j")
z = complex(input())
x = abs(z)
y = cmath.phase(z)
g = z.conjugate
print (g)
