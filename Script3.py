#Importamos las librerias necesarias
import numpy as np
from matplotlib import pyplot as plt

#Generamos 100 puntos equidistantes entre 0 y 2 Pi (ciclo completo de un circulo) con 'linspace'
theta = np.linspace(0, 2*np.pi, 100)

# Se calculan las coordenadas x e y utilizando ecuaciones parametricas que describen la forma de un corazon.
x = 16 * (np.sin(theta)**3)
y = 13 * np.cos(theta) - 5 * np.cos(2*theta)-np.cos(4*theta)



# Trazamos un grafico de lineas con las coordenadas x e y calculadas.
plt.plot(x,y)

# Cambiamos el color del grafico a rojo 
plt.plot(x, y, color='red')

#Agregamos un titulo a la grafica
plt.title('Corasao')

#Mostramos en pantalla la grafica
plt.show()