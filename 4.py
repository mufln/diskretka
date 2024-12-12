from math import log2, ceil

import numpy as np
#Запросить у пользователя количество информационных разрядов и рассчитать для него количество проверочных.

#Методом Хемминга закодировать произвольную информационную комбинацию, заданного размера, построив порождающую и проверочную матрицы.

#Внести ошибку в один из разрядов кодового вектора; найти синдром; найти и исправить ошибку.

def hamming_code(k):
    # Расчет количества проверочных бит
    r = ceil(log2(k+1+ceil(log2(k+1))))

    n = k + r  # Общая длина кодовой комбинации

    # Порождающая матрица
    G = np.zeros((k, n), dtype=int)
    for i in range(k):
        G[i][i] = 1

    H = np.zeros((r, n), dtype=int)
    count = 1
    grades = set(2**i for i in range(100))
    grades.union(set(2**i-1 for i in range(100)))
    for i in range(k):
        if i<k:
            while count in grades:
                count += 1
            bin(count)[2:].zfill(r)
            H[:,i] = [int(x) for x in bin(count)[2:].zfill(r)[::-1]]
            count += 1

    for i in range(n-1, n-r-1, -1):
        H[i-r-1,i] = 1

    # Проверочная матрица
    G[:, -r:] = H.transpose()[:k]

    return G, H, n



def correct_error(encoded_message, error_position):
    corrected_message = encoded_message.copy()
    corrected_message[error_position] ^= 1
    return corrected_message


# Запрашиваем количество информационных разрядов
k = int(input("Введите количество информационных разрядов: "))
G, H, n = hamming_code(k)

print(f"Порождающая матрица:\n{G}")
print(f"Проверочная матрица:\n{H}")

# Просим пользователя ввести информационную комбинацию
message = [int(i) for i in input("Введите информационную комбинацию: ")]
print(f"\nИнформационная комбинация: {message}")

# Кодируем сообщение методом Хемминга
encoded_message = message @ G % 2
print(f"Закодированное сообщение: {encoded_message}")

# Вносим ошибку в одно из положений
error_position = np.random.randint(0, n)
print(f"Внесена ошибка в разряд {error_position}")
faulty_encoded_message = encoded_message.copy()
faulty_encoded_message[error_position-1] ^= 1
print(faulty_encoded_message)

# Вычисляем синдром
syndrome_vector = faulty_encoded_message @ H.transpose() % 2
print(f"Синдром ошибки: {syndrome_vector}")

# Находим положение ошибки
# detected_error_position = int(sum([i*2**j for i, j in enumerate(syndrome_vector[::-1])]))
# if detected_error_position is not None:
#     print(f"Ошибка найдена в разряде {detected_error_position}")
# else:
#     print("Ошибка не найдена")

# Исправляем ошибку
corrected_message = faulty_encoded_message
faulty_col = 0
for i in range(n):
    if H[:, i].tolist() == syndrome_vector.tolist():
        faulty_col = i+1

corrected_message[faulty_col-1] ^= 1
print(f"Исправленное кодовое слово: {corrected_message}")