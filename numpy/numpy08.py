
import numpy as np

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(f'original array: \n{a}')
a = np.delete(a, 1, 0)
a = np.delete(a, 0, 1)

print(f'after delete: \n{a}')

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
])
print(f'original array: \n{b}')

b = np.delete(b, np.s_[::2], 0)
print(f'after delete: \n{b}')
