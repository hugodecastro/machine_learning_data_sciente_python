
import numpy as np

l = [20, 30, 40, 50]
print(l[1:3]) # [30, 40]
print(l[::2]) # [20, 40]

a = np.array(l)
print(a[1:3]) # [30 40]
print(a[::2]) # [20 40]

l2 = l[:]

l2[0] = 1000
print(l) # [20, 30, 40, 50]
print(l2) # [1000, 30, 40, 50]

b = a[:]
b[0] = 1000
print(a) # [1000   30   40   50]
print(b) # [1000   30   40   50]
b[:] = 42
print(a) # [42 42 42 42]

c = a.copy()
print(c) # [42 42 42 42]
print(a) # [42 42 42 42]

c[0] = 100000
print(c) # [100000     42     42     42]
print(a) # [42 42 42 42]