

import numpy as np
import matplotlib.pyplot as plt

salarios_a = np.array([100, 200, 400, 300])
salarios_b = np.array([50, 300, 500, 450])
salarios_c = np.array([200, 150, 300, 700])


plt.plot(salarios_a, c='Black', ls='--', marker='s', ms=8, label='Salários A')
plt.plot(salarios_b, c='Red', ls='--', marker='^', ms=8, label='Salários B')
plt.plot(salarios_c, c='Green', ls='--', marker='o', ms=8, label='Salários C')
plt.legend(loc='upper left')
plt.show()
