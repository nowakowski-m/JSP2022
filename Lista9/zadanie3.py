import numpy as np
import matplotlib.pyplot as plt

V0 = int(input("Podaj początkową prędkość: "))
alfa = int(input("Podaj kąt rzutu: "))

Vy0 = np.sin(np.radians(alfa)) * V0
Vx0 = np.sin(np.radians(alfa)) * V0
tpol = Vy0/9.81
Hmax = Vy0*tpol - (9.81*tpol**2)/2
X = Vx0*2*tpol
T = 2*tpol
print('\n',"Wysokość maksymalna =",Hmax,'\n',"Zasięg rzutu =",X,'\n',"Czas lotu =",T)
Tcale = np.linspace(0,T,100)

plt.subplot(1, 3, 1)
Vx = np.linspace(Vx0,Vx0,100)
Vy = np.abs(Vy0 - 9.81*Tcale)

plt.title("Prędkości")
plt.plot(Tcale,Vy, label="Vy(t)")
plt.plot(Tcale,Vx, label="Vx(t)")
plt.legend()

plt.subplot(1,3,2)
plt.title("Położenie")
X = Vx0*Tcale
Y = Vy0*Tcale - (9.81*Tcale**2)/2
plt.plot(Tcale,X, label="x(t)")
plt.plot(Tcale,Y, label="y(t)")
plt.legend()

plt.subplot(1,3,3)
plt.title("Wykres toru ruchu")
plt.plot(X,Y, label="y(x)")

plt.legend()
plt.show()