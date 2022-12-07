# Zadanie 4

twoList = []

for make2List in range(2,100,2):
    twoList.append(make2List)

for checkEle in twoList:
    if checkEle % 3 == 0 and checkEle % 5 == 0:
        print ("SykBzyk")
    elif checkEle % 3 == 0:
        print ("Syk")
    elif checkEle % 5 == 0:
        print ("Bzyk")
    else:
        print (checkEle)