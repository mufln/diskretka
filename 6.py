# Напишите вспомогательную программу
# построения таблицы простых чисел меньших 256 с помощью решета Эратосфена.
from math import ceil, gcd
from random import randint


# Выясните с помощью метода Ферма,
# являются ли n произвольных чисел простыми; в случае составного числа разложите его на множители.

# Для произвольного большого
# простого числа p выясните вопрос о его простоте:

# - с помощью теста Соловея – Штрассена;

# - с помощью теста Лемана;

# - с помощью теста Рабина – Миллера;

# - с помощью непосредственной проверки


def eratosfen(n):
    l = [i for i in range(2, n)]
    i = 0
    c = 2
    while (len(l) > i):
        if l[i] * c in l:
            l.remove(l[i] * c)

        if l[i] * c > n:
            i += 1
            c = 1
        c += 1
    return l


print("Получим список простых чисел до 256")
print(eratosfen(256))


def fermat(n):
    a = ceil(n ** 0.5)

    while True:
        b_squared = a ** 2 - n
        b = int(b_squared ** 0.5)
        if b ** 2 == b_squared:
            break
        a += 1
    p = a + b
    q = a - b
    return p, q


print("С помощью метода Ферма разложим числа на множители")
for i in (1010101, 12321, 5959, 1493, 13):
    p, q = fermat(i)
    print(f"{i} = {p} * {q}")


def j(a, n):
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0


def soloway(n):
    a = 3
    if gcd(n, a) != 1:
        return False
    o = (a**((n-1)//2))%n
    if o == j(a,n):
        return "50/50"
    else:
        return False

print("Тест соловея-штрассена для n=13")
print(soloway(13))


def lemann(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for a in range(2, n):
        if gcd(a, n) > 1:
            return False
        if pow(a, (n - 1) // 2, n) not in [1, n - 1]:
            return False
    return True

print("Тест леманна для n=13")
print(lemann(13))


def rabip(p):
    a = p-1
    b = 0
    while a>0:
        if a%2==0:
            a = a/2
            b += 1
        else:
            break
    m = (p-1)/2**b
    a = 3
    j= 0
    z = (a**m)%p
    if z == 1 or z == p - 1:
        return "50/50"
    while (True):
        if j>0 and z==1:
            return False
        j+=1
        if j<b and z!=p-1:
            z = (z**2)%p
            continue
        if z==p-1:
            return True
        if z==b and z!=p-1:
            return False



print("Тест Рабина для p=13")
print(rabip(13))