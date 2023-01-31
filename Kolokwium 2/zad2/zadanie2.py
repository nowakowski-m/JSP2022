import os

os.system("clear")

def dzielniki(test_int):
    dzielniki_string = "Dzielniki liczby " + str(test_int) + ":\n"
    for dzielnik in range ((test_int), 0, (-1)):
        if (test_int % dzielnik) == 0:
            dzielniki_string += (str(dzielnik) + " ")

    dzielniki_string += "\n"

    return dzielniki_string

def liczba_pierwsza(test_int2, dzielniki_str):
    it_is = "Liczba " + str(test_int2) + " jest liczbą pierwszą.\n"
    its_not = "Liczba " + str(test_int2) + " nie jest liczbą pierwszą.\n"

    if test_int2 > 1:
        dzielniki_list = dzielniki_str.split("\n")
        dzielniki_list = dzielniki_list[1]
        dzielniki_list = dzielniki_list.split(" ")

        if (len(dzielniki_list)) == 3:
            if dzielniki_list[0] == str(test_int2) or dzielniki_list[1] == str(test_int2):
                if dzielniki_list[0] == "1" or dzielniki_list[1] == "1":
                    return it_is

                else:
                    return its_not
            else:
                return its_not
        else:
            return its_not
    else:
        return its_not

def doskonala(test_int3, dzielniki_str2):
    it_is = "Liczba " + str(test_int3) + " jest liczbą doskonałą.\n"
    its_not = "Liczba " + str(test_int3) + " nie jest liczbą doskonałą.\n"
    
    dzielniki_list = dzielniki_str2.split("\n")
    dzielniki_list = dzielniki_list[1]
    dzielniki_list = dzielniki_list.split(" ")
    sum = 0

    for dzielnik in dzielniki_list:
        if dzielnik == "":
            continue
        if int(dzielnik) < test_int3:
            sum += int(dzielnik)

    if sum == test_int3:
        return it_is
    else:
        return its_not


try:
    num_to_check = int(input("Wprowadź liczbę naturalną: "))
    
    if num_to_check <= 0:
        num_to_check = ""

    print("\n")

    print(dzielniki(num_to_check))
    print(liczba_pierwsza(num_to_check, dzielniki(num_to_check)))
    print(doskonala(num_to_check, dzielniki(num_to_check)))

except:
    print("Wprowadzony argument nie jest liczbą naturalną.")