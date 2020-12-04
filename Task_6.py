from random import randint
n = 3
matrix = [[randint(1, 9) for j in range(n)]for i in range(n)]

"""Найти максимальный элемент матрицы."""

print(matrix)
print(max(map(max, matrix)))
