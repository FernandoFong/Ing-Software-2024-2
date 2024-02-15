import matplotlib
matplotlib.use('agg')  # Usa el backend 'agg' como alternativa
import matplotlib
matplotlib.use('Qt5Agg')  # Establece el backend interactivo

import matplotlib.pyplot as plt
import numpy as np

def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 3, 100)
X, Y = np.meshgrid(x, y)
Z = rosenbrock(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Rosenbrock Function')
plt.show()
