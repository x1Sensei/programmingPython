import numpy as np
# # import pandas as pd

# # a=np.array([1, 2, 3])
# # print(type(a))
# # print(a.shape)

# # print(a[0], a[1], a[2])

# # a[0] = 5
# # a[1] += 100
# # a[2] *= 2
# # a[2] -= 10
# # print(a)


# # b = np.array([[1,2,3],[1,2,3]])
# # print(type(b))
# # print(b.shape)
# # print(b)

# # print(b[1, 1])
# # b[1, 1] += 100

# # print

# # a=np.zeros((4,5))
# # print(a)
# # print(a.shape)

# # b=np.ones((4,5))
# # print(b)
# # print(b.shape)


# # c=np.eye(5)
# # print(c)

# # d=np.full((4,5), 7)
# # print(d)
# # print(d.shape)

# # e=np.random.random((4,5))
# # print(e)
# # print(e.shape)

# # # una matriz de 3 * 4 con valores enteros ramdom


# # f=np.random.randint(0, 10, (3,4))
# # print(f)
# # print(f.shape)

# # # Extraer elementos de una matriz




# # # Matriz aleatoria de 3x4
# # f = np.random.randint(0, 10, (3,4))
# # print("Matriz f:")
# # print(f)


# # elem = f[1, 2]
# # print("\nElemento en fila 1, col 2:", elem)


# # fila0 = f[0, :]
# # print("\nFila 0 completa:", fila0)


# # col1 = f[:, 1]
# # print("\nColumna 1 completa:", col1)


# # submatriz = f[0:2, 1:3]
# # print("\nSubmatriz (filas 0-1, columnas 1-2):")
# # print(submatriz)


# g = np.random.randint(1, 20, (5,6))
# print("Matriz g:")
# print(g)
# submatriz_g = g[1:4, 2:5]
# print("\nSubmatriz de g (filas 1-3, columnas 2-4):")
# print(submatriz_g)


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Matriz a:")
# print(a)

# mask = (a % 2 == 0)
# print("\nElementos pares de a:")
# print(a[mask])

# b = a[a > 5]
# print("\nElementos de a mayores que 5:")
# print(b)

# Arreglo de 7 x 7 cuyo elmentos vayan del 0 al 100, y el filtro va a hacer los elementos del 40 al 60, que no sean aleatorios


h = np.linspace(0, 100, 49).astype(int).reshape(7, 7)
print("Matriz h:")
print(h)

mask_h = (h >= 40) & (h <= 60)
print("\nElementos de h entre 40 y 60:")
print(h[mask_h])




