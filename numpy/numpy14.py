
import numpy as np

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(f'elements bigger than 3: \n {a[a>3]}')

idx = (a > 2)

print(idx)