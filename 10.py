# Сгенерировать два больших простых числа

# Выполнить с числами операции сложения,
# вычитания, умножения, деления, вычисления остатка
# от деления одного числа на другое, возведения одного из чисел в степень n по модулю m.

def gen(k, m):
    a = [1 for i in range(k)]
    n = m + 2 * k - 2
    d = 3
    b = []
    while (not d ** 2 > n):
        j = 1
        r = m % d
        if r > 0 and r % 2 == 1:
            j = j + (d - r) // 2
        if m <= d:
            j = j + d
        for i in range(j, k, d):
            a[i] = 0
        if d % 6 == 1:
            d += 4
        else:
            d += 2
    for i in range(k - 1, 0, -1):
        if a[i] == 1:
            b.append(m + 2 * i - 2)
    return b


def pow(a, m):
    K = m - 2
    B = 1
    A = a
    while (True):
        q = K // 2
        r = K - 2 * q
        K = q
        if r == 0:
            A = (A ** 2) % m
        else:
            B = A * B % m
            if K == 0:
                return B
            A = (A ** 2) % m


a, b = gen(100000, 3)[0:2]
print(f"{a}+{b}={a + b}")
print(f"{a}-{b}={a - b}")
print(f"{a}*{b}={a * b}")
print(f"{a}/{b}={a / b}")
print(f"{a}%{b}={a % b}")
print(f"\nВозьмем степень 2323040, модуль 2323042, число 618970019642690137449562111")
# совпадает с калькулятором
print(pow(618970019642690137449562111, 2422))
