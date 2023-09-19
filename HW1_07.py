import numpy as np

#7 Створіть дві матриці розміром 2x2 та 2x3, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та перемножте їх між собою.
matrix1 = np.random.randint(1, 10, size=(2, 2))
matrix2 = np.random.randint(1, 10, size=(2, 3))

print("Матриця 1:")
print(matrix1)
print("Матриця 2:")
print(matrix2)

result = np.dot(matrix1, matrix2)

print("Результат множення:")
print(result)
