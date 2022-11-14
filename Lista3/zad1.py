x = str(input("Enter a letter: "))

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
samo = ['a','e','i','o','u','y']

while len(x) > 1:
    x = str(input("Enter max. 1 character: "))

while x in num:
    x = str(input("Enter a letter, not a number: "))

if x in samo:
    print ("Your letter is samogłoska.")
else:
    print ("Your letter is spółgłoska.")