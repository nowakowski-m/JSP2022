n = int(input("Wprowadź liczbę N elementów ciągu: "))

ciag = list([0, 1])

x = 0
y = 1
z = 0
while z <= 0.5*n:
   x = x + y
   y = y + x
   ciag.append(x)
   ciag.append(y)
   z += 1

print(ciag[0:n])