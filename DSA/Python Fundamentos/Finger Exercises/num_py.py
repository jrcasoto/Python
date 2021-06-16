import numpy as np

# 1 dimensão -> vetor; 2 dimensões -> matriz; 3 dimensões -> tensor
vetor1 = np.array([0,1,2,3,4,5,6,7,8])
type(vetor1)

# Operando em arrays
vetor1.cumsum()
vetor1.size
vetor1.shape # Unidimensional

vetor2 = np.arange(0., 4.5, .5) # Similar a funcao range, mas com números reais
print(vetor2)
vetor3 = np.arange(1, 10, 0.25)
print(vetor3)

print(np.zeros(10)) # Criar matriz com zeros

x = np.eye(3) # Matriz identidade
x

d = np.diag(np.array([1,2,3,4])) # Matriz diagonal
d

# É possível fazer arrays com booleanos, strings ou números complexos

np.linspace(0,10)
print(np.linspace(0, 10, 15))
print(np.logspace(0, 5, 10))

# Matrizes
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.shape) # Ordem da matriz

matriz1 = np.ones((2,3))
print(matriz1)

lista = [[1,2,3], [4,5,6], [7,8,9]]
matriz2 = np.matrix(lista) # Conversão explícita para matriz
print(matriz2)
np.shape(matriz2) # Equivalente ao matriz2.shape

# Atributos
matriz2.size
matriz2.dtype
matriz2.itemsize
matriz2.nbytes
print(matriz2[2,1]) # Slicing

x = np.array([1,2], dtype= np.float64)
print(x.dtype)

print(np.random.rand(10))

# Impressão de dados em gráficos
import matplotlib.pyplot as plt
plt.show((plt.hist(np.random.rand(1000))))

print(np.random.rand(5,5))
plt.show(plt.hist(np.random.rand(1000)))
img = np.random.rand(30,30)
plt.imshow(img, cmap = plt.cm.hot)
plt.colorbar()