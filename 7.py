from string import ascii_lowercase
import re

s = input("Введите строку: ")
s.lower()
s = re.sub(r'[^a-z]', '', s)
print("Строка в нижнем регистре")
print(s)


def caesar(s, k):
    return ''.join([ascii_lowercase[(ascii_lowercase.index(c) + k) % 26] for c in s])


s = caesar(s, 3)
print("\nСтрока с цезарем")
print(s)
s = caesar(s, -3)
print("Расшифрованная строка с цезарем")
print(s)

available = set(ascii_lowercase)
d = {i: available.pop() for i in ascii_lowercase}
d1 = {d[i]: i for i in d.keys()}

def hard(s, encode=True):
    if encode:
        return ''.join([d[c] for c in s])
    return ''.join([d1[c] for c in s])


print("\nСтрока в сложном шифре")
s = hard(s)
print(s)
print("Расшифрованная строка в сложном шифре")
s = hard(s, encode=False)
print(s)
