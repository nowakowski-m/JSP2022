import numpy as np

functions = np.array([

    [1, 2, 3, -2, -1],
    [3, 5, 5, -3, -9],
    [2, 3, 2, 0, -8],
    [2, 6, 7, -5, 1],
    [1, 2, 6, -4, -10]

    ])

equals = np.array([6,2,-5,17,12])

equations = np.linalg.solve(functions, equals)

print("x = ",equations[0])
print("z = ",equations[1])
print("y = ",equations[2])
print("t = ",equations[3])
print("u = ",equations[4])