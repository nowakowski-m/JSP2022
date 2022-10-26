studenci = ["Kasia", "Basia", "Marek", "Darek"]
studenci.append ("Józek")
studenci1 = ["Ania", "Basia"]
studenci.extend (studenci1)

studenci.sort()

print (studenci[3])
print (studenci[:2])
print (studenci[(len(studenci)-2):len(studenci)-0])

while "Basia" in studenci:
	studenci.remove("Basia")
	
print (studenci)

print ("Ilość studentów: ", len(studenci))

finalList = studenci

print (finalList)
