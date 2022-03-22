
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
]) 

a = np.array_split(a, 2, axis=0)

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

b = np.array_split(b, 2, axis=0)
for array in b:
    print(array)