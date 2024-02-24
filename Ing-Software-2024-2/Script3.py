import matplotlib.pyplot as plt
import numpy as np

def graficar_funcion():
    x = np.linspace(0, 5, 100)
    y = x**(2/3)

    plt.plot(x, y, label='f(x) = x^(2/3)')
    plt.title('Gráfica de f(x) = x^(2/3)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()  # Muestra la informacion de la grafica
    plt.grid(True)  # Muestra la cuadrícula
    plt.show()  # Muestra la gráfica

# Función para graficar
graficar_funcion()