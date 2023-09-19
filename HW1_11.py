import numpy as np

# 11 Створіть матрицю розміром 2x3 та вектор розміром 3, заповніть їх випадковими дійсними числами в діапазоні від 0 до 1 та перемножте матрицю на вектор.
matrix = np.random.rand(2, 3)

vector = np.random.rand(3)
print("Початкова матриця:")
print(matrix)
print("Початковий вектор:")
print(vector)

result = np.dot(matrix, vector)

print("Результат множення матриці на вектор:")
print(result)