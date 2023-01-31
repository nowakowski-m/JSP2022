import sys
import os

os.system("clear")

should_continue = True

if (len(sys.argv) < 2):
    print("Nie podano argumentu - pliku do odczytu.")
    should_continue = False
elif (len(sys.argv) > 2):
    print("Podano zbyt wiele argumentów, oczekiwany: 1.")
    should_continue = False


if should_continue == True:

    file_name = sys.argv[1]

    try:
        with open(file_name, "r") as my_file:
            check_string = my_file.read()
            my_file.close()

            palindrom_list = []
            not_palindrom_list = []
            palindrom_string = ''
            not_palindrom_string = ''

            check_list = check_string.split("\n")

            for x in check_list:
                temp_x = x[::-1]
                if temp_x == x:
                    palindrom_list.append(x)
                else:
                    not_palindrom_list.append(x)

            for y in palindrom_list:
                palindrom_string += (y + "\n")

            for z in not_palindrom_list:
                not_palindrom_string += (z + "\n")

            with open("palindromy.txt", 'w') as p_file:
                p_file.write(palindrom_string)
                p_file.close()
            
            with open("nie_palindromy.txt", 'w') as not_p_file:
                not_p_file.write(not_palindrom_string)
                not_p_file.close()

            print("Palindrom list:\n" + palindrom_string)
            print("Not-palindrom list:\n" + not_palindrom_string)

    except IOError:
        print("Nie ma takiego pliku, lub jest w innej lokalizacji.")