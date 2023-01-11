from os import path


def pesel_load() -> str:
    open_file = open(
        "PESEL.txt", 'r')
    pesel = open_file.read()
    open_file.close()

    return pesel


def pesel_save(pesel_data):
    save_file = open("ENCODED_PESEL.TXT", 'w')
    save_file.write(pesel_data)
    save_file.close()


def pesel_group() -> list:
    pesel_list = pesel_load().split("\n")
    for ele in range(len(pesel_list)):
        if pesel_list[ele] == "":
            pesel_list.remove(pesel_list[ele])

    return pesel_list


def ten_pesel_check():
    months = list(range(81, 92))+list(range(1, 12)) + \
        list(range(21, 32)) + list(range(41, 52))+list(range(61, 72))
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]

    true_date = False
    pesel_correct = False

    if path.exists("PESEL.txt") == True:
        for list_ele in range(len(pesel_group())):
            possible_pesel = False
            check_m = int(pesel_group()[list_ele]
                          [2] + pesel_group()[list_ele][3])
            check_d = int(pesel_group()[list_ele]
                          [4] + pesel_group()[list_ele][5])
            if check_m in months:
                if 1 <= check_d <= 31:
                    possible_pesel = True

            if possible_pesel == True:
                temp_pesel = ""
                pesel_year = ""
                pesel_month = ""
                pesel_day = ""
                temp_correct = 0
                for pesel_ele in range(len(pesel_group()[list_ele])):
                    match pesel_ele:
                        case 0:
                            weight = 1
                        case 1:
                            weight = 3
                        case 2:
                            weight = 7
                        case 3:
                            weight = 9
                        case 4:
                            weight = 1
                        case 5:
                            weight = 3
                        case 6:
                            weight = 7
                        case 7:
                            weight = 9
                        case 8:
                            weight = 1
                        case 9:
                            weight = 3
                        case 10:
                            weight = 0

                    temp_multiply = (
                        int(pesel_group()[list_ele][pesel_ele]))*weight

                    if len(str(temp_multiply)) == 1:
                        temp_pesel += str(temp_multiply)
                    if len(str(temp_multiply)) == 2:
                        temp_pesel += (str(temp_multiply))[1]

                for correct_check_ele in range(len(temp_pesel)):
                    temp_correct += int(temp_pesel[correct_check_ele])

                if len(str(temp_correct)) == 1:
                    last_pesel_num = 10 - temp_correct

                if len(str(temp_correct)) == 2:
                    last_pesel_num = 10 - int(str(temp_correct)[1])

                if str(last_pesel_num) == (pesel_group()[list_ele])[10]:
                    pesel_year += (pesel_group()[list_ele])[0]
                    pesel_year += (pesel_group()[list_ele])[1]
                    pesel_month += (pesel_group()[list_ele])[2]
                    pesel_month += (pesel_group()[list_ele])[3]

                    if int(pesel_month) >= 1 and int(pesel_month) <= 12:
                        pesel_year = "19" + pesel_year
                    elif int(pesel_month) >= 21 and int(pesel_month) <= 32:
                        pesel_year = "20" + pesel_year
                        pesel_month = str(int(pesel_month)-20)
                    elif int(pesel_month) >= 41 and int(pesel_month) <= 52:
                        pesel_year = "21" + pesel_year
                        pesel_month = str(int(pesel_month)-40)
                    elif int(pesel_month) >= 61 and int(pesel_month) <= 72:
                        pesel_year = "22" + pesel_year
                        pesel_month = str(int(pesel_month)-60)
                    elif int(pesel_month) >= 81 and int(pesel_month) <= 92:
                        pesel_year = "18" + pesel_year
                        pesel_month = str(int(pesel_month)-80)
                    else:
                        print((pesel_group()[list_ele]) +
                              ": Pesel niepoprawny.")
                        break

                    check_y = int(pesel_year)
                    check_m = int(pesel_month)
                    if check_m in months_31:
                        if check_d <= 31 and check_d >= 1:
                            true_date = True
                    if check_m in months_30:
                        if check_d <= 30 and check_d >= 1:
                            true_date = True
                    if check_m == 2:
                        if check_y % 4 == 0 and check_y % 100 == 0 and check_y % 400 == 0:
                            if check_d <= 29 and check_d >= 1:
                                true_date = True
                        elif check_y % 4 == 0 and check_y % 100 != 0:
                            if check_d <= 29 and check_d >= 1:
                                true_date = True
                        elif check_y % 4 != 0:
                            if check_d <= 28 and check_d >= 1:
                                true_date = True
                        elif check_y % 4 == 0 and check_y % 100 == 0 and check_y % 400 != 0:
                            if check_d <= 28 and check_d >= 1:
                                true_date = True

                    if true_date == True:

                        pesel_day += (pesel_group()[list_ele])[4]
                        pesel_day += (pesel_group()[list_ele])[5]
                        pesel_sex_check = int((pesel_group()[list_ele])[9])
                        if pesel_sex_check % 2 == 0:
                            pesel_sex = "Kobieta"
                        if pesel_sex_check % 2 == 1:
                            pesel_sex = "Mężczyzna"

                        print((pesel_group()[list_ele]) + ": Pesel poprawny.")
                        pesel_data = "nr PESEL: " + (pesel_group()[list_ele]) + "\nData urodzenia: " + \
                            pesel_day + "-" + pesel_month + "-" + pesel_year + "\t płeć: " + pesel_sex + "\n"
                        pesel_save(pesel_data)
                        # tu dorobic zeby dodawalo do nowych linijek i stworzyc skrypt
                        # testowy ktory zgeneruje 10 peseli do nowego pliku
                        pesel_correct = True

                else:
                    print((pesel_group()[list_ele]) +
                          ": Pesel niepoprawny.")

            else:
                print((pesel_group()[list_ele]) + ": Pesel niepoprawny.")

    if path.exists("PESEL.txt") == False:
        print("Blad! Plik nie istnieje, lub jest w innej lokalizacji.")


def pesel_check(what_pesel):
    months = list(range(81, 92))+list(range(1, 12)) + \
        list(range(21, 32)) + list(range(41, 52))+list(range(61, 72))
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]

    true_date = False
    pesel_correct = False

    for list_ele in range(len(what_pesel)):
        possible_pesel = False
        check_m = int(what_pesel[2] + what_pesel[3])
        check_d = int(what_pesel[4] + what_pesel[5])
        if check_m in months:
            if 1 <= check_d <= 31:
                possible_pesel = True

        if possible_pesel == True:
            temp_pesel = ""
            pesel_year = ""
            pesel_month = ""
            pesel_day = ""
            temp_correct = 0
            for pesel_ele in range(len(what_pesel)):
                match pesel_ele:
                    case 0:
                        weight = 1
                    case 1:
                        weight = 3
                    case 2:
                        weight = 7
                    case 3:
                        weight = 9
                    case 4:
                        weight = 1
                    case 5:
                        weight = 3
                    case 6:
                        weight = 7
                    case 7:
                        weight = 9
                    case 8:
                        weight = 1
                    case 9:
                        weight = 3
                    case 10:
                        weight = 0

                temp_multiply = (
                    int(what_pesel[pesel_ele]))*weight

                if len(str(temp_multiply)) == 1:
                    temp_pesel += str(temp_multiply)
                if len(str(temp_multiply)) == 2:
                    temp_pesel += (str(temp_multiply))[1]

            for correct_check_ele in range(len(temp_pesel)):
                temp_correct += int(temp_pesel[correct_check_ele])

            if len(str(temp_correct)) == 1:
                last_pesel_num = 10 - temp_correct

            if len(str(temp_correct)) == 2:
                last_pesel_num = 10 - int(str(temp_correct)[1])

            if str(last_pesel_num) == (what_pesel)[10]:
                pesel_year += (what_pesel)[0]
                pesel_year += (what_pesel)[1]
                pesel_month += (what_pesel)[2]
                pesel_month += (what_pesel)[3]

                if int(pesel_month) >= 1 and int(pesel_month) <= 12:
                    pesel_year = "19" + pesel_year
                elif int(pesel_month) >= 21 and int(pesel_month) <= 32:
                    pesel_year = "20" + pesel_year
                    pesel_month = str(int(pesel_month)-20)
                elif int(pesel_month) >= 41 and int(pesel_month) <= 52:
                    pesel_year = "21" + pesel_year
                    pesel_month = str(int(pesel_month)-40)
                elif int(pesel_month) >= 61 and int(pesel_month) <= 72:
                    pesel_year = "22" + pesel_year
                    pesel_month = str(int(pesel_month)-60)
                elif int(pesel_month) >= 81 and int(pesel_month) <= 92:
                    pesel_year = "18" + pesel_year
                    pesel_month = str(int(pesel_month)-80)
                else:
                    return pesel_data

                check_y = int(pesel_year)
                check_m = int(pesel_month)
                if check_m in months_31:
                    if check_d <= 31 and check_d >= 1:
                        true_date = True
                if check_m in months_30:
                    if check_d <= 30 and check_d >= 1:
                        true_date = True
                if check_m == 2:
                    if check_y % 4 == 0 and check_y % 100 == 0 and check_y % 400 == 0:
                        if check_d <= 29 and check_d >= 1:
                            true_date = True
                    elif check_y % 4 == 0 and check_y % 100 != 0:
                        if check_d <= 29 and check_d >= 1:
                            true_date = True
                    elif check_y % 4 != 0:
                        if check_d <= 28 and check_d >= 1:
                            true_date = True
                    elif check_y % 4 == 0 and check_y % 100 == 0 and check_y % 400 != 0:
                        if check_d <= 28 and check_d >= 1:
                            true_date = True

                if true_date == True:

                    pesel_day += (what_pesel)[4]
                    pesel_day += (what_pesel)[5]
                    pesel_sex_check = int((what_pesel)[9])
                    if pesel_sex_check % 2 == 0:
                        pesel_sex = "Kobieta"
                    if pesel_sex_check % 2 == 1:
                        pesel_sex = "Mężczyzna"

                    pesel_data = "nr PESEL: " + (what_pesel) + "\nData urodzenia: " + \
                        pesel_day + "-" + pesel_month + "-" + pesel_year + "\t płeć: " + pesel_sex + "\n"

                    pesel_correct = True

                    return pesel_data

            else:
                return pesel_correct

        else:
            return pesel_correct

ten_pesel_check()