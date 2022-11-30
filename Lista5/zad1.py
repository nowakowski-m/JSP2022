def words_to_num(numWords: str) -> int:

    liczby = ["zero", "jeden", "dwa", "trzy", "czter", "pie", "szes", "siedem", "osiem", "dziewie"]
    rozw = ["dziescia", "dziesci", "dziesiat"]
    space = " "

    if "dziesiec" in numWords:
        print ("Twoja liczba: ", 10)

    if len(numWords) <= 8:

        for x in range (0, 10):
            if liczby[x] in numWords:
                print ( "Twoja liczba: ", x )
                break

    if len(numWords) > 8:

        if "nascie" in numWords:
            for x in range (0, 10):
                if liczby[x] in numWords:
                    print ( "Twoja liczba:", 1, end = "" )
                    print (x)
                    break

        elif space in numWords:
            for y in range (1, 3):
                if rozw[y] in numWords:
                    for x in range (0, 10):
                        splited = numWords.split()
                        if liczby[x] in splited[0]:
                            for z in range (0, 10):
                                if liczby[z] in splited[1]:
                                    print ( "Twoja liczba:", x, end = "" )
                                    print (z)

        else:
            for y in range (0, 3):
                if rozw[y] in numWords:
                    for x in range (0, 10):
                        if liczby[x] in numWords:
                            print ( "Twoja liczba:", x, end = "" )
                            print (0)
                            break

numWords = str(input("Wprowadz slownie liczbe od 1 do 59: "))
words_to_num(numWords)