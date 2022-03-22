import numpy as np

print("Array")
a = np.array([10, 20, 30, 40])

print(a) # [10 20 30 40]
print(type(a)) # <class 'numpy.ndarray'>
print("\n")

print("Matriz")
mat = np.array([[1, 2], [3, 4]])

print(f'matriz: \n{mat}') # [[1 2]
                        # [3 4]]
print(f'último registro: {mat[1][1]}') # 4
print(f'último registro: {mat[-1][-1]}') # 4
print(f'última linha: {mat[1,:]}') # [3 4]
print(f'primeira coluna: {mat[:,0]}') # [1 3]
print(f'matriz transposta: \n{mat.transpose()}')
print("\n")

print('Operações Básicas')
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(f'adição: \n{m1 + m2}')
print(f'subtração: \n{m1 - m2}')
print(f'multiplicação: \n{m1 * m2}')

m3 = np.array([1,2,3,4,5])
print(f'soma dos elementos: {m3.sum()}')
print(f'índice maior elemento: {m3.argmax()}')
print(f'índice menor elemento: {m3.argmin()}')