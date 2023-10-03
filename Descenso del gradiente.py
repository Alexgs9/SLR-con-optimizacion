# -*- coding: utf-8 -*-

#Hecho por Alexandro Gutierrez Serna

import numpy as np
import math
import matplotlib.pyplot as plt


#Implementacion del descenso del gradiente

# Funcion de tarea: 10 - math.exp(-(a**2 + 3*b**2))
def f(a,b):
    return 10 - np.exp(-(a**2 + 3*b**2))

# Derivada parcial con respecto a "a": 2 * a * math.exp(-a**2 - 3*b**2)
def df_da(a,b):
    return 2 * a * math.exp(-a**2 - 3*b**2)

# Derivada parcial con respecto a "b": 6 * b * math.exp(-3 * b**2 - a**2)
def df_db(a,b):
    return 6 * b * math.exp(-3 * b**2 - a**2)

# Punto inicial
a = -1
b = 1
alpha = 0.1
n_iteraciones = 100

iteraciones = []
a_valores = []
b_valores = []
y = []

# Iteraciones para llegar a obtener el global minimo
for i in range(n_iteraciones):
    print('------------------------')
    print('iteración ', str(i+1))
    a = a - alpha * df_da(a, b)
    b = b - alpha * df_db(a, b)

    a_valores.append(a)
    b_valores.append(b)
    
    # Almacenar iteración y valor correspondiente
    y.append(f(a, b))
    iteraciones.append(i+1)

    # Imprimir resultados
    print('a = ', str(a), ', b = ', str(b), ', y = ', str(f(a, b)))

a_valores = np.array(a_valores)
b_valores = np.array(b_valores)
y = np.array(y)


#Graficando

# Crear una cuadrícula de valores para a y b
a_malla = np.linspace(-2, 2, 100)
b_malla = np.linspace(-2, 2, 100)
a_grid, b_grid = np.meshgrid(a_malla, b_malla)
# Evaluar la función en cada punto de la cuadrícula
z_grid = f(a_grid, b_grid)


#Se crea la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(a_grid, b_grid, z_grid, cmap='viridis', alpha=0.5)

ax.scatter(a_valores, b_valores, y, c='b', marker='o')

ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('Y')

ax.view_init(elev=60, azim=30)

plt.show()
