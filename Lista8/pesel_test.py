import zad3 as base
import zad4 as functions

def pesel_test(multiple_times):

    repeat = 0
    next_lines = []
    
    while repeat != multiple_times:

        pesel_to_check = base.create_pesel()

        if functions.pesel_check(pesel_to_check) != False:

            repeat += 1

            data_to_save = functions.pesel_check(pesel_to_check)

            next_lines.append(data_to_save)

    save_next_pesel = open("PESEL_TEST.txt", 'w')
    save_next_pesel.writelines(next_lines)
    save_next_pesel.close()

pesel_test(15)