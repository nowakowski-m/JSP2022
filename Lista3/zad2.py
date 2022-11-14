x = int(input("Wprowadz liczbe: "))

if x % 2 == 0:
    print("Liczba jest parzysta.")
if x % 2 != 0:
    print("Liczba jest nieparzysta.")

while x % 2 == 0:
    print("Liczba jest parzysta.")
    break

while x % 2 != 0:
    print("Liczba jest nieparzysta.")
    break