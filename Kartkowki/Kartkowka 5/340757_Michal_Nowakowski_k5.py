class Zespolona:
    @staticmethod

    def dodaj(comp_num1, comp_num2):
        if "+" in str(comp_num1):
            comp_list1 = (str(comp_num1)).split("+")
            znak1 = "+"
        if "-" in str(comp_num1):
            comp_num = "To nie jest dodawanie."

        re1 = comp_list1[0]
        im1 = comp_list1[1]
        im1 = im1.replace("i", '')

        if "+" in str(comp_num2):
            comp_list2 = (str(comp_num2)).split("+")
            znak2 = "+"
        if "-" in str(comp_num2):
            comp_num = "To nie jest dodawanie."

        re2 = comp_list2[0]
        im2 = comp_list2[1]
        im2 = im2.replace("i", '')

        if znak1 == znak2:
            znak = "+"
        if znak1 != znak2:
            znak = "-"

        if znak == "+":
            re = int(re1) + int(re2)
            im = int(im1) + int(im2)
            comp_num = str(re) + znak + str(im) + "i"
        
        if znak == "-":
            re = int(re1) + int(re2)
            im = int(im1) - int(im2)
            comp_num = str(re) + str(im) + "i"

        return comp_num

    def odejmij(comp_num1, comp_num2):
        if "+" in str(comp_num1):
            comp_num = "To nie jest odejmowanie."
        if "-" in str(comp_num1):
            comp_list1 = (str(comp_num1)).split("-")
            znak1 = "-"

        re1 = comp_list1[0]
        im1 = comp_list1[1]
        im1 = im1.replace("i", '')

        if "+" in str(comp_num2):
            comp_num = "To nie jest odejmowanie."
        if "-" in str(comp_num2):
            comp_list2 = (str(comp_num2)).split("-")
            znak2 = "-"

        re2 = comp_list2[0]
        im2 = comp_list2[1]
        im2 = im2.replace("i", '')

        if znak1 == znak2:
            znak = "+"
        if znak1 != znak2:
            znak = "-"

        if znak == "+":
            re = int(re1) + int(re2)
            im = int(im1) + int(im2)
            comp_num = str(re) + znak + str(im) + "i"
        
        if znak == "-":
            re = int(re1) + int(re2)
            im = int(im1) - int(im2)
            comp_num = str(re) + str(im) + "i"

        return comp_num

    def mnoz(comp_num1, comp_num2):
        if "*" in str(comp_num1):
            comp_list1 = (str(comp_num1)).split("*")
            znak1 = "*"
        if "/" in str(comp_num1):
            comp_num = "To nie jest mnożenie."

        re1 = comp_list1[0]
        im1 = comp_list1[1]
        im1 = im1.replace("i", '')

        if "*" in str(comp_num2):
            comp_list2 = (str(comp_num2)).split("*")
            znak2 = "*"
        if "/" in str(comp_num2):
            comp_num = "To nie jest mnożenie."

        re2 = comp_list2[0]
        im2 = comp_list2[1]
        im2 = im2.replace("i", '')

        if znak1 == znak2:
            znak = "*"

        if znak == "*":
            re = int(re1) * int(re2)
            im = int(im1) * int(im2)
            comp_num = str(re) + znak + str(im) + "i"

        return comp_num

    def dziel(comp_num1, comp_num2):
        if "*" in str(comp_num1):
            comp_num = "To nie jest dzielenie."
        if "/" in str(comp_num1):
            comp_list1 = (str(comp_num1)).split("/")
            znak1 = "/"

        re1 = comp_list1[0]
        im1 = comp_list1[1]
        im1 = im1.replace("i", '')

        if "*" in str(comp_num2):
            comp_num = "To nie jest dzielenie."
        if "/" in str(comp_num2):
            comp_list2 = (str(comp_num2)).split("/")
            znak2 = "/"

        re2 = comp_list2[0]
        im2 = comp_list2[1]
        im2 = im2.replace("i", '')

        if znak1 == znak2:
            znak = "/"

        if znak == "/":
            re = int(re1) / int(re2)
            im = int(im1) / int(im2)
            comp_num = str(re) + znak + str(im) + "i"

        return comp_num

    def argument(comp_num1):
        if "*" in str(comp_num1):
            comp_num = "To nie jest dzielenie."
        if "/" in str(comp_num1):
            comp_list1 = (str(comp_num1)).split("/")
            znak1 = "/"

        re1 = comp_list1[0]
        
        return re1

comp = Zespolona()

x = str(input("1st complex num: "))
y = str(input("2nd complex num: "))

# print(comp."funckja"(x, y))
print(comp.dodaj(x,y))