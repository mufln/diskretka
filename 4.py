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
    for i in range(r):
        for j in range(n):
            if j-k == i:
                H[i, j] = 1
            elif j+1>k:
                H[i, j] = 0
            else:
                if r>3:
                    H[i, j] = 1
                else:
                    H[i, j] = np.random.randint(0, 2)

    print(H)
    # Проверочная матрица
    G[:, -r:] = H.transpose()[:k]

    return G, H, n


def encode(message, G):
    encoded_message = message @ G % 2
    return encoded_message


def syndrome(encoded_message, H):
    syndrome_vector = encoded_message @ H.T % 2
    return syndrome_vector


def find_error(syndrome_vector, H):
    error_position = None
    for i in range(H.shape[1]):
        if np.array_equal(syndrome_vector, H[:, i]):
            error_position = i
            break
    return error_position


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
encoded_message = encode(message, G)
print(f"Закодированное сообщение: {encoded_message}")

# Вносим ошибку в одно из положений
error_position = np.random.randint(0, n)
error_position = 2
print(f"Внесена ошибка в разряд {error_position}")
faulty_encoded_message = encoded_message.copy()
faulty_encoded_message[error_position] ^= 1

# Вычисляем синдром
syndrome_vector = syndrome(faulty_encoded_message, H)
print(f"Синдром ошибки: {syndrome_vector}")

# Находим положение ошибки
detected_error_position = find_error(syndrome_vector, H)
if detected_error_position is not None:
    print(f"Ошибка найдена в разряде {detected_error_position}")
else:
    print("Ошибка не найдена")

# Исправляем ошибку
corrected_message = correct_error(faulty_encoded_message, detected_error_position)
print(f"Исправленное кодовое слово: {corrected_message}")
