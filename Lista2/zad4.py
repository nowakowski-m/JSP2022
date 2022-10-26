x = input("Wprowadź napis: ")
y = x[0]
z = (x.replace(y, "$"))
print (z.replace("$", y, 1))
