import math

class Kolo:
    def __init__(self, r):
        self.r = r
    
    def pole(self):
        return (self.r)**2*math.pi
    def obwod(self):
        return (self.r)*2*math.pi
        
input_r = float(input("Wprowadź promień koła: "))        
users_circle = Kolo(input_r)

print ("Pole: " + str(users_circle.pole()))
print ("Obwód: " + str(users_circle.obwod()))