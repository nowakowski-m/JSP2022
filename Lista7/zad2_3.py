import time
import random
import os

os.system("clear")

n = int(input("Wprowadz liczbe n-elementów listy: "))

random_nums = []
sorted_list = []
random_nums2 = []

start_insert_time = time.perf_counter()

for x in range (0, n):
    x = random.randint(0, 20)
    random_nums.append(x)
    random_nums2.append(x)

for y in range (len(random_nums)):
    sorted_list.append(min(random_nums))
    random_nums.remove(min(random_nums))

finish_insert_time = time.perf_counter() - start_insert_time

start_bubbles_time = time.perf_counter()

for i in range(len(random_nums2)):
    for j in range(0, len(random_nums2)-i-1):
        if random_nums2[j] > random_nums2[j+1]:
            random_nums2[j], random_nums2[j+1] = random_nums2[j+1], random_nums2[j]

finish_bubbles_time = time.perf_counter() - start_bubbles_time

if finish_insert_time < finish_bubbles_time:
    print("\nCzas dla metody wstawiania: \x1b[32m" + str(finish_insert_time) + "\x1b[0m")
    print("\nCzas dla metody bąbelkowej: \x1b[31m" + str(finish_bubbles_time) + "\x1b]0m")

if finish_insert_time > finish_bubbles_time:
    print("\nCzas dla metody wstawiania: \x1b[31m" + str(finish_insert_time) + "\x1b[0m")
    print("\nCzas dla metody bąbelkowej: \x1b[32m" + str(finish_bubbles_time) + "\x1b]0m")

if finish_insert_time == finish_bubbles_time:
    print("\nCzas dla metody wstawiania: \x1b[32m" + str(finish_insert_time) + "\x1b[0m")
    print("\nCzas dla metody bąbelkowej: \x1b[32m" + str(finish_bubbles_time) + "\x1b]0m")