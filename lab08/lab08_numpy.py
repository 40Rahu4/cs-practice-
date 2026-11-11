import numpy as np

# Задание 1. Создание векторов и матриц

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print("hours:")
print(hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

# Задание 2. Индексы и срезы в векторе

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:")
print(hours[2:6])
print("Каждый второй элемент:")
print(hours[::2])
print("Массив в обратном порядке:")
print(hours[::-1])

# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)

print("Значение во второй строке и третьем столбце:", temperatures[1, 2])
print("Первая строка:")
print(temperatures[0])
print("Последний столбец:")
print(temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2×2:")
print(temperatures[:2, 1:3])

# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)

first_rows = matrix[:3]
last_rows = matrix[-2:]
first_columns = matrix[:, :2]
middle_fragment = matrix[1:4, 2:5]
bottom_right = matrix[-2:, -2:]

print("Первые три строки:")
print(first_rows)
print("shape:", first_rows.shape)

print("Последние две строки:")
print(last_rows)
print("shape:", last_rows.shape)

print("Первые два столбца:")
print(first_columns)
print("shape:", first_columns.shape)

print("Строки 1–3, столбцы 2–4:")
print(middle_fragment)
print("shape:", middle_fragment.shape)

print("Правый нижний блок 2×2:")
print(bottom_right)
print("shape:", bottom_right.shape)

# Задание 5. Изменение массива с помощью срезов

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()

# .copy() нужна, чтобы changed_hours стал независимой копией hours.
# Иначе срез вернёт представление исходного массива, и изменение
# changed_hours также изменит исходный hours.
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:")
print(changed_hours)
print("Исходный hours:")
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Итоговая матрица:")
print(changed_matrix)
print("Исходная матрица:")
print(matrix)

# Задание 6. Изменение формы

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)