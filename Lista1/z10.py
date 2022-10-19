import cmath
z = 1j
print ("sin ", cmath.sin(z))
print ("cos ", cmath.cos(z))
print ("sin^2(z)+cos^2(z)", cmath.sin(z)**2+cmath.cos(z)**2)
if cmath.sin(z)**2+cmath.cos(z)**2==1:
	print ("Zaleznosc spelniona")
else:
	print ("Zaleznosc niespelniona")
