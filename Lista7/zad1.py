import time

n = int(input("Wprowadź liczbę N elementów ciągu: "))

ciag = list([0, 1])

x = 0
y = 1
z = 0

recurency_time = time.time()

while z <= n:
   x = x + y
   y = y + x
   ciag.append(x)
   ciag.append(y)
   z += 1

recurency = (time.time() - recurency_time)

iteracy_time = time.time()

for z in range (0, n):
    x = x + y
    y = y + x
    ciag.append(x)
    ciag.append(y)
    z += 1

iteracy = (time.time() - iteracy_time)

if iteracy > recurency:
    print('\n' + "recurency time: \x1b[32m" + str(recurency) + '\x1b[0m' + '\n')
    print("iteracy time: \x1b[31m"+ str(iteracy) + '\x1b[0m' + '\n')

if recurency > iteracy:
    print('\n' + "recurency time: \x1b[31m" + str(recurency) + '\x1b[0m' + '\n')
    print("iteracy time: \x1b[32m"+ str(iteracy) + '\x1b[0m' + '\n')

if recurency == iteracy:
    print('\n' + "recurency time: \x1b[32m" + str(recurency) + '\x1b[0m' + '\n')
    print("iteracy time: \x1b[32m"+ str(iteracy) + '\x1b[0m' + '\n')