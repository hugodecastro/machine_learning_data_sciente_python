
import numpy as np

m1 = np.array([[1,2,3], [4, 5, 6]])
m2 = np.array([[7,8,9], [10, 11, 12]])

print(f'divisão: \n {m2 / m1}')
print(f'arredondando: \n {np.matrix.round(m2 / m1)}')

print(f'ao quadrado: {m1 ** 2}')