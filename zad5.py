x = input("Wprowadź elementy do listy, oddzielając je od siebie spacją  : ")

list = x.split()
list.sort()

def permutation(y, z=0):
   if z == len(y):
      print (y)
   else:
      for i in range(z, len(y)):
         y[z], y[i] = y[i] ,y[z]
         permutation(y, z+1)
         y[z], y[i] = y[i], y[z]

permutation(list)