import sortowanie as sr
import random
import time
import os

os.system("clear")

random_nums = []

for x in range (0, 1000):
    x = random.randint(0, 1000)
    random_nums.append(x)

start_insert_time = time.perf_counter()

sr.insert_type(random_nums)

finish_insert_time = time.perf_counter() - start_insert_time

start_bubbles_time = time.perf_counter()

sr.bubble_type(random_nums)

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