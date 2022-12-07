# Zadanie 2

A = [[1,2], {'jeden':'1', 'dwa':'2'}]

x = ''

for createX in range(0,97):
    x += '1'

x = int(x)

A[1]['jeden'] = x

print(A)

