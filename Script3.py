import numpy as np
import matplotlib.pyplot as plt

# Va a definir la función cuadrática
def funcion_cuadratica(x):
    return x**2 - 3*x + 2

#Vamos a generar los valores que va a tener x
x = np.linspace(-5, 5, 100)

# Vamos a generar lo valores que le corresponden a y
y = funcion_cuadratica(x)

# Lo siguiente nos permite gráficar correctamente la funcion.
plt.plot(x, y, label="$f(x) = x^2 - 3x + 2$")
plt.title("Gráfica de la función cuadrática $f(x) = x^2 - 3x + 2$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

