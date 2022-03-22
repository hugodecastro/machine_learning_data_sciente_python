
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])
print(f'original array: \n{a}')

a = np.repeat(a, 2)
print(f'array with 2 repetitions: \n{a}')
