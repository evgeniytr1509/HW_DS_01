import numpy as np
#15 Створіть дві матриці розміром 4x4, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та знайдіть їхню різницю.
matrix1 = np.random.randint(1, 10, size=(4, 4))
matrix2 = np.random.randint(1, 10, size=(4, 4))

# Виводимо початкові матриці
print("Матриця 1:")
print(matrix1)
print("Матриця 2:")
print(matrix2)

# Знаходимо різницю матриць
result = matrix1 - matrix2

# Виводимо результат різниці
print("Різниця матриць:")
print(result)