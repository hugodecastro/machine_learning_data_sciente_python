
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('./numpy/data/iris.data', delimiter=',', usecols=(0,1,2,3))

print(data)

print(f'sepals length: {data[:,0]}')

print(f'iris-setosa sepals length: {data[:50,0]}')

plt.plot(data[:50,0], c='Red', ls=':', marker='s', ms=8, label='Iris-setosa Sepal Len')
plt.plot(data[50:100,0], c='Black', ls=':', marker='o', ms=8, label='Iris-versicolor Sepal Len')
plt.legend()
plt.show()

