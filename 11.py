from math import gcd
from string import ascii_lowercase
#Сгенерировать два простых числа.

#Получить открытый и закрытый ключи алгоритма RSA.

#Подготовить открытый текст для шифрования и разбить его на блоки.

#Провести шифрование текста

#Расшифровать текст

def pow(a, m, k=0):
    if k == 0:
        k = m-2
    K = k
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

p, q = gen(100, 3)[0:2]

sub = {i:a+10 for a,i in enumerate(ascii_lowercase)}
isub = {a+10:i for a,i in enumerate(ascii_lowercase)}
old = "oaoammm"
print("Зашифруем строку")
print(old)
new = ''
for i in old:
    new+=str(sub[i])
print("Числовой вид")
print(new)

N = p * q

c = 0
blocks = []
for i in new:
    if (c*10+int(i))>=N:
        blocks.append(c)
        c=int(i)
        continue
    c=c*10+int(i)
if c>0:
    blocks.append(c)

print("Блоки")
print(blocks)

phi = (p-1)*(q-1)
e = 2
while(gcd(phi,e)!=1):
    e+=1

encrypted = []
for i in blocks:
    encrypted.append((i**e)%N)

print("Зашифрованные блоки")
print(encrypted)


d=1
while(not e*d%phi==1):
    d+=1

decrypted = []
for i in encrypted:
    decrypted.append(i**d%N)

print("Восстановленные блоки")
print(decrypted)


print("Расшифрованная строка")
s = ''.join([str(i) for i in decrypted])

decs = ''
c = ''
for i in s:
    c += i
    if int(c) in isub:
        decs+=isub[int(c)]
        c = ''

print(decs)


