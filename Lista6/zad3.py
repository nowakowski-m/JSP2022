import os

def look_and_say(n):
    whole_sequence = ""
    n_line = "1"
    for i in range(n-1):
        current_number = n_line
        n_line = ""
        current_digit = current_number[0]
        count = 1
        for j in range(1, len(current_number)):
            if current_number[j] == current_digit:
                count += 1
            else:
                n_line += str(count) + current_digit
                current_digit = current_number[j]
                count = 1
        n_line += str(count) + current_digit
        whole_sequence += n_line + "\n"
    return whole_sequence

os.system("clear")

n = int(input("Wprowadź liczbę n wyrazów ciągu Look and Say: "))

print("\n1\n" + look_and_say(n))