import numpy as np

print("--- ЗАДАНИЕ 1 ---")
array1 = np.random.randint(-10, 11, (4, 4))
array2 = np.random.randint(-10, 11, (4, 4))
array3 = np.random.randint(-10, 11, (4, 4))

combined_array = np.stack([array1, array2, array3], axis=0)

print("Объединенный массив формы (3, 4, 4):")
print(combined_array)

assert combined_array.shape == (3, 4, 4), "Ошибка: размер должен быть (3, 4, 4)"

print("--- ЗАДАНИЕ 2 ---")
B = np.random.randint(1, 10, (2, 3, 4))
print("Оригинальный тривимерный массив B:")
print(B)

B_reshaped = B.reshape(6, 4)
print("Массив после изменения формы на 6x4:")
print(B_reshaped)

B_flattened = B_reshaped.flatten()
print("Сплющенный (одномерный) массив:")
print(B_flattened)

print("\n--- ЗАДАНИЕ 3 ---")
C = np.random.randint(1, 10, (3, 3, 3))
print("Оригинальный массив C:")
print(C)

sum_axis0 = np.sum(C, axis=0)
print("Сумма по оси 0 (слои):")
print(sum_axis0)

sum_axis1 = np.sum(C, axis=1)
print("Сумма по оси 1 (столбцы):")
print(sum_axis1)

total_sum = np.sum(C)
print("Общая сумма всех элементов в массиве:")
print(total_sum)