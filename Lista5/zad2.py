def num_to_words(num:int) -> str:
    
    num_str = str(num)
    num_len = len(num_str)
    num_list = list(num_str)

    unitys = {
        0:"",
        1:"jeden",
        2:"dwa",
        3:"trzy",
        4:"cztery",
        5:"pięć",
        6:"sześć",
        7:"siedem",
        8:"osiem",
        9:"dziewięć",
        10:"dziesięć",
        11:"jedenaście",
        12:"dwanaście",
        13:"trzynaście",
        14:"czternaście",
        15:"piętnaście",
        16:"szesnaście",
        17:"siedemnaście",
        18:"osiemnaście",
        19:"dziewiętnaście"
    }

    tens = {
        0:"",
        2:"dwadzieścia",
        3:"trzydzieści",
        4:"czterdzieści",
        5:"pięćdziesiąt",
        6:"sześćdziesiąt",
        7:"siedemdziesiąt",
        8:"osiemdziesiąt",
        9:"dziewięćdziesiąt"
    }

    hundreds = {
        0:"",
        1:"sto",
        2:"dwieście",
        3:"trzysta",
        4:"czterysta",
        5:"pięćset",
        6:"sześcset",
        7:"siedemset",
        8:"osiemset",
        9:"dziewięćset"
    }

    if num_len == 1 or 2 and num in unitys.keys():
        return(unitys[num])

    if num_len == 2:
        a = int(num_list[0])
        if a in tens.keys():
            b = int(num_list[1])
            if b in unitys.keys():
                return(tens[a] + " " + unitys[b])

    if num_len == 3:
        a = int(num_list[0])
        if a in hundreds.keys():
            b = int(num_list[1])
            if b in tens.keys():
                c = int(num_list[2])
                if c in unitys.keys():
                    return(hundreds[a] + " " + tens[b] + " " + unitys[c])

    if num_len == 4:
        a = int(num_list[1])
        if a in hundreds.keys():
            b = int(num_list[2])
            if b in tens.keys():
                c = int(num_list[3])
                if c in unitys.keys():
                    return("tysiąc " + hundreds[a] + " " + tens[b] + " " + unitys[c])


num = int(input("Wprowadź liczbę od 1 do 1999: "))
if num >= 1 and num <= 1999:
    print(num_to_words(num))
else:
    print("Liczba nie należy do podanego przedziału!")