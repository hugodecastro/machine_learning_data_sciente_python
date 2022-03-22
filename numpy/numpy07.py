
import numpy as np

a = np.array(
    [1,2,3]
)

a = np.append(a, [4,5,6])
print(a)

b = np.array([
    [1, 2],
    [3, 4]
])

b = np.append(b, [[5,6]], axis=0)
print(b)