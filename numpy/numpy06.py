
import numpy as np

arr = np.array([1, 2, 3])

np.insert(arr, 1, 10)

a = np.array([[1,2], [3,4]])

print(f'soma do eixo 0: {a.sum(axis=0)}')
print(f'soma do eixo 1: {a.sum(axis=1)}')

b = np.insert(a, 1, 5, axis=1)
print(b)
c = np.insert(a, 1, 5, axis=0)
print(c)
