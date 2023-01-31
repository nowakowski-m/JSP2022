import time
import os

os.system("clear")

class Obywatel():
    def __init__(self, imie, nazwisko, data):
        # data format: DDMMYYYY
        self.imie = imie
        self.nazwisko = nazwisko
        self.data = data

    def __str__(self):
        data_str = str(self.data)

        local_time = time.localtime()
        year = local_time.tm_year
        month = local_time.tm_mon
        day = local_time.tm_mday

        if month < int(data_str[2] + data_str[3]):
            wiek = int(year) - ((int(data_str[4] + data_str[5] + data_str[6] + data_str[7]) + 1))
        if month == int(data_str[2] + data_str[3]):
            if day < int(data_str[0] + data_str[1]):
                wiek = int(year) - ((int(data_str[4] + data_str[5] + data_str[6] + data_str[7]) + 1))
            if day == int(data_str[0] + data_str[1]):
                wiek = int(year) - (int(data_str[4] + data_str[5] + data_str[6] + data_str[7]))
            if day > int(data_str[0] + data_str[1]):
                wiek = int(year) - (int(data_str[4] + data_str[5] + data_str[6] + data_str[7]))
        if month > int(data_str[2] + data_str[3]):
            wiek = int(year) - (int(data_str[4] + data_str[5] + data_str[6] + data_str[7]))

        r_str = "Obywatel/ka " + str(self.imie) + " " + str(self.nazwisko) + ", " + str(wiek) + " lat, urodzony " + data_str[0:2] + "-" + data_str[2:4] + "-" + data_str[4:8] + "."

        if wiek < 0:
            r_str = "Podana data urodzenia jest niepoprawna."

        return r_str

osob = Obywatel("Michał", "Nowakowski", 20112003)

print(osob, "\n")