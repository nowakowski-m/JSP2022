from bs4 import BeautifulSoup
import requests
import re
import os

os.system("clear")

basic_url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
res = requests.get(basic_url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

xml = str(soup.findAll('a', href=re.compile(
    'https://static.nbp.pl/'))).split('"')[1]

class Kursy():
    def __init__(self, xml_file):

        self.xml_file = xml_file
        self.waluty = []
        self.wartosc_waluty = []
        self.skrot_waluty = []
        self.wartosc_pln = []

        self.xml_page = requests.get(self.xml_file).content
        self.new_soup = BeautifulSoup(self.xml_page, "xml")

        self.y = list(self.new_soup.find_all(text=True))
        self.z = []

        for x in range(0, len(self.y)):
            if self.y[x] != "\n":
                self.z.append(self.y[x])

        del self.z[0]
        self.actual_date = (self.z).pop(0)

        for regroup in range(0, len(self.z)-4, 4):
            self.waluty.append(self.z[regroup])
            self.wartosc_waluty.append(self.z[regroup+1])
            self.skrot_waluty.append(self.z[regroup+2])
            self.wartosc_pln.append(self.z[regroup+3])

    def available_exchanges(self):
        if len(self.waluty) == len(self.wartosc_waluty) == len(self.skrot_waluty) == len(self.wartosc_pln):
            
            self.build_string = ("--------------------------------" + "\n")
            self.build_string += ("---------- " + str(self.actual_date) + " ----------" + "\n")
            self.build_string += ("--------------------------------" + "\n")
            
            for self.x in range(0, len(self.waluty)):
                self.build_string += ("Waluta: " + str(self.waluty[self.x]) + "\n")
                self.build_string += ("Skrót: " + str(self.skrot_waluty[self.x]) + "\n")
                self.build_string += ("Wartość (" + str(self.skrot_waluty[self.x]) + "): ") + str(self.wartosc_waluty[self.x] + "\n")
                self.build_string += ("Wartość (PLN): " + str(self.wartosc_pln[self.x]) + "\n")
                self.build_string += ("--------------------------------" + "\n")
        
        else:
            self.build_string = "Błąd z odczytem danych z pliku XML."

        return self.build_string

    def pln_to_other(self, amount, other):

        self.other = other
        self.amount = amount
        self.corrected_amount = ""
        self.corrected_pln_price = ""

        for self.y in range(0, len(str(self.amount))):
            if (str(self.amount))[self.y] == ",":
                self.corrected_amount += "."
            else:
                self.corrected_amount += (str(self.amount)[self.y])

        for self.x in range(0, len(self.skrot_waluty)):

            self.convert_string = ("--------------------------------" + "\n")

            if (str(self.skrot_waluty[self.x])) == (str(self.other).upper()):

                for self.z in range(0, len(str(self.wartosc_pln[self.x]))):
                    if self.wartosc_pln[self.x][self.z] == ",":
                        self.corrected_pln_price += "."
                    else:
                        self.corrected_pln_price += self.wartosc_pln[self.x][self.z]

                self.convert_string += (str(self.corrected_amount) + "PLN   =   " + ((str(round(float(self.corrected_amount)/float(self.corrected_pln_price), 2))) + str(self.other) + "\n"))
                self.convert_string += ("--------------------------------" + "\n")
                
                break

        return self.convert_string

    def sth_to_other(self, amount, curr1, curr2):

        self.amount = amount
        self.curr1 = curr1
        self.curr2 = curr2
        self.corrected_amount1 = ""
        self.corrected_amount2 = ""
        self.corrected_pln_amount1 = ""
        self.corrected_pln_amount2 = ""

        for self.x in range(0, len(str(self.amount))):
            if (str(self.amount))[self.x] == ",":
                self.corrected_amount1 += "."
            else:
                self.corrected_amount1 += (str(self.amount)[self.x])

        for self.y in range(0, len(self.waluty)):
            if (str(self.skrot_waluty[self.y])) == (str(self.curr1).upper()):
                self.mark1 = self.y
                break
        
        for self.z in range(0, len(self.waluty)):
            if (str(self.skrot_waluty[self.z])) == (str(self.curr2).upper()):
                self.mark2 = self.z
                break

        for self.i in range(0, len(str(self.wartosc_pln[self.mark1]))):
            if self.wartosc_pln[self.mark1][self.i] == ",":
                self.corrected_pln_amount1 += "."
            else:
                self.corrected_pln_amount1 += self.wartosc_pln[self.mark1][self.i]
        
        for self.i in range(0, len(str(self.wartosc_pln[self.mark2]))):
            if self.wartosc_pln[self.mark2][self.i] == ",":
                self.corrected_pln_amount2 += "."
            else:
                self.corrected_pln_amount2 += self.wartosc_pln[self.mark2][self.i]

        curr1_to_pln = ((float(self.corrected_amount1)) * (float(self.corrected_pln_amount1)))
        curr2_from_pln = ((float(curr1_to_pln)) / (float(self.corrected_pln_amount2)))
        self.convert_string2 = ("--------------------------------" + "\n")
        self.convert_string2 += (((str(self.corrected_amount1)) + (str(self.skrot_waluty[self.mark1])) + "   =   " + (str(round(float(curr2_from_pln), 2)))) + (str(self.skrot_waluty[self.mark2])) + "\n")
        self.convert_string2 += ("--------------------------------" + "\n")
        
        return self.convert_string2

kursy_walut = Kursy(xml)

# ()
print(kursy_walut.available_exchanges())
# (kwota, waluta)
print(kursy_walut.pln_to_other("50,09", "EUR"))
# (kwota, waluta ktorej podajemy kwote, waluta druga)
print(kursy_walut.sth_to_other(50.93, "EUR", "USD"))