
import numpy as np

val1, val2, val3 = np.loadtxt('./numpy/data/dados.txt', skiprows=1, unpack=True)

print(f'valores 1: {val1}')
print(f'valores 2: {val2}')
print(f'valores 3: {val3}')

print("\n")

values = np.genfromtxt('./numpy/data/dados2.txt', skip_header=1, filling_values=-99)

print(f'values: {values}')
