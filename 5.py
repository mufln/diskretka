from math import log2, ceil

import numpy as np


def from_binarr(n):
    return int(''.join([str(x) for x in n]), 2)


# Запросить у пользователя количество битов
k = [int(x) for x in input("введите сообщение: ")]
r = ceil(log2(len(k)+1+ceil(log2(len(k)+1))))

n = len(k) + r+1
print(n)
# делаем матрицу
g = np.zeros((ceil(log2(n)) + 1, n), dtype=int)
for i in range(ceil(log2(n)) + 1):
    for j in range(n):
        if i > 0 and (2 ** (i - 1)) & j:
            g[i][j] = 1
print(g)
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

rand = np.random.randint(0, n)
print(f"Получим b`, изменим b[-{rand}]")
b1[-rand]^= 1
print(b1)
# считаем синдром
s = b1 @ g[1:,:].transpose() % 2
print(f"Синдром {s}")

faulty_col = 0
for i in range(n):
    if g[1:, i].tolist() == s.tolist():
        faulty_col = i+1
b1[faulty_col-1] ^= 1
print(f"Исходная последовательность\n", b1)





