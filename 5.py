from math import log2, ceil

import numpy as np


def from_binarr(n):
    return int(''.join([str(x) for x in n]), 2)


# Запросить у пользователя количество битов
n = int(input("Введите число битов: "))
k = [int(x) for x in input("введите сообщение: ")]
# делаем матрицу
g = np.zeros((ceil(log2(n)) + 1, n), dtype=int)
for i in range(ceil(log2(n)) + 1):
    for j in range(n):
        if i > 0 and (2 ** (i - 1)) & j:
            g[i][j] = 1

# находим b
indexes = []
for i in range(n):
    if g[:, i].sum() > 1:
        indexes.append(i)
        g[:, i][0] = g[:, i][1]

for i in range(n):
    if g[:, i].sum() == 1:
        c = list(g[:, i]).index(1)
        g[:, i][0] = list(k * g[c, indexes]).count(1) % 2

print("Получим b")
print(g[0])
b1 = g[0].copy()

print("Получим b`, изменим b[-1] = 0")
b1[-1] = 0
print(b1)
# считаем синдром
s = [((int(''.join([str(i) for i in b1]),2)&int(''.join([str(i) for i in a]),2))^1)%2 for a in g[1:]]
print(f"Синдром {s}")

b1[from_binarr(s)] = 1 if b1[from_binarr(s)] == 0 else 0
print(f"Исходная последовательность\n", b1)
