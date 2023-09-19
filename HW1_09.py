import numpy as np


#9 Створіть матрицю розміром 4x4, заповніть її випадковими дійсними числами в діапазоні від 0 до 1 та транспонуйте її.
matrix = np.random.rand(4, 4)

print("Початкова матриця:")
print(matrix)
transposed_matrix = np.transpose(matrix)

print("Транспонована матриця:")
print(transposed_matrix)

