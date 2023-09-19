import numpy as np

#8 Створіть матрицю розміром 3x3, заповніть її випадковими цілими числами в діапазоні від 1 до 10 та знайдіть її обернену матрицю
matrix = np.random.randint(1, 10, size=(3, 3))

print("Початкова матриця:")
print(matrix)

inverse_matrix = np.linalg.inv(matrix)
print("Обернена матриця:")
print(inverse_matrix)

