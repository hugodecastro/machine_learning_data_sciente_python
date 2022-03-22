
import numpy as np
import matplotlib.pyplot as plt

salario = np.array([100, 200, 300, 500, 400, 150])
print(salario)

# Ploting with matplot
plt.plot(salario)


plt.plot(salario, 
         c='Black', # cor da linha
         ls='--', # tipo da linha
         marker='s' # marcador
    )
plt.show()