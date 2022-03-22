import numpy as np

m = [
    [5,4,7], 
    [0,3,4], 
    [0,0,6]
]

for l in m:
    print(l)

p1 = [20, 30, 40, 15]
p2 = [100, 23, 45, 23]
p3 = [92, 22, 34, 12]
p4 = [12, 34, 12, 43]

p = np.array([p1,p2,p3,p4])
print(p)

# Criando array com dado intervalo
my_data = np.arange(0,20)

print(my_data)

# Transformando array em matriz
mat1 = np.reshape(my_data, (5,4))
print(mat1)

print(p.item(5))

m1 = ["python", "é", "legal"]
m2 = ["guido", "van", "rossum"]
m3 = [10, 20, 30]

m = np.array([m1, m2, m3])
print(m)
