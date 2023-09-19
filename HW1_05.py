import numpy as np

#5 Створіть два одновимірних масиви розміром 5, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та виконайте на них поелементні операції додавання, віднімання та множення.
array1 = np.random.randint(1, 10, size=5)
array2 = np.random.randint(1, 10, size=5)

# Виконуємо поелементні операції додавання, віднімання та множення
sum_result = array1 + array2
subtract_result = array1 - array2
multiply_result = array1 * array2

# Виводимо результати операцій
print("Сума масивів:", sum_result)
print("Різниця масивів:", subtract_result)
print("Добуток масивів:", multiply_result)


