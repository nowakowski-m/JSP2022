import random as r

def create_pesel() -> str:

    temp_pesel = ""
    
    for _ in range (0, 11):
        y = r.randint(0, 9)
        temp_pesel += str(y)

    return temp_pesel

def save_ten_pesels() -> str:

    ten_pesels = ""
    
    for _ in range (0, 10):
        ten_pesels += (create_pesel() + "\n")

    save_file = open("PESEL.txt", 'w')
    save_file.write(ten_pesels)
    save_file.close()

save_ten_pesels()