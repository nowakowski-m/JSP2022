x = input("Wprowadź elementy do listy, oddzielając je od siebie spacją  : ")

list = x.split()
list = [*set(list)]
list.sort()
print(list)