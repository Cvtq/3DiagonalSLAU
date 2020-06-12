import numpy as np
import random

# 03.06 Без варианта (случайная генерация)

n = 5
cMatrix = np.zeros((n, n))

# Создаем вектор свободных коэффициентов
fArray = np.random.randint(low=1, high=25, size=5)

# Отступы для коэффициентов a,b,c
offsets = [-1, 1, 0]

# Цикл заполнения СЛАУ случайными значениями
for i in range(n):

    # Генерируем одну строку матрицы случайным образом
    for offset in offsets:
        if offset >=0 and offset < 5:
            if offsets.index(offset) == 2:
                cMatrix[i][offset] = random.randint(1, 25)
            else:
                cMatrix[i][offset] = -1 * random.randint(1, 25)

    # Увеличиваем все отступы на 1
    for j in range(len(offsets)):
        offsets[j] += 1

print("Матрица коэффициентов: \n", cMatrix)
print("Вектор свободных коэффициентов: \n", fArray)

# Прямой ход алгоритма
alpha = [0] * n
beta = [0] * n
alpha[0] = cMatrix[0][1] / cMatrix[0][0]  # b[0] / c[0]
beta[0] = fArray[0] / cMatrix[0][0]       # f[0] / c[0]

for i in range(1, n - 1):
    denominator = cMatrix[i][i] + cMatrix[i][i - 1] * alpha[i - 1] # Ci - Ai * Alpha(i)
    alpha[i] = cMatrix[i][i + 1] / denominator
    beta[i] = (fArray[i] + cMatrix[i][i - 1] * beta[i - 1]) / denominator

# Обратный ход
x = [0] * n
x[n - 1] = (fArray[n - 1] + alpha[n - 1] * beta[n - 1]) / (cMatrix[n - 1][n - 1] + cMatrix[n - 1][n - 2] * alpha[n - 1])

for i in reversed(range(n - 1)):
    x[i] = alpha[i] * x[i + 1] + beta[i]
    x = np.array(x)

print("X = \n ", x)