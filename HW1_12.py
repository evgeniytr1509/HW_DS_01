import numpy as np

# 12 Створіть дві матриці розміром 2x2, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та виконайте їхнє поелементне множення.
matrix1 = np.random.randint(1, 10, size=(2, 2))
matrix2 = np.random.randint(1, 10, size=(2, 2))

print("Матриця 1:")
print(matrix1)
print("Матриця 2:")
print(matrix2)

# поелементне множення матриць
result = np.multiply(matrix1, matrix2)

print("Результат поелементного множення:")
print(result)

