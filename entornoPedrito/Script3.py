import matplotlib.pyplot as plt
import numpy as np
import math

def distribucion_binomial(n, p):
    k = np.arange(0, n+1)
    probabilidades = np.array([(math.factorial(n) / (math.factorial(k) * math.factorial(n-k))) * (p**k) * ((1-p)**(n-k)) for k in k])
    return k, probabilidades

n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo

k, probabilidades = distribucion_binomial(n, p)

plt.bar(k, probabilidades)
plt.title('Distribución Binomial (n={}, p={})'.format(n, p))
plt.xlabel('Número de éxitos')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()

