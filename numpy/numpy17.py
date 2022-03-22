
import numpy as np

values = np.genfromtxt('./numpy/data/file.csv', skip_header=1, delimiter=';')

print(values)