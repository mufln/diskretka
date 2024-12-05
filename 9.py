import random
#Выбрать фрагмент открытого текста.


# Сгенерировать гамму шифра требуемой длины
# одним из генераторов псевдослучайных последовательностей.

#Зашифровать фрагмент открытого текста.

#Дешифровать зашифрованный текст


salt = random.randint(0, 255)

print("Строка для шифрования")
s = "oaoammm"
print(s)

cyphered = ""
for i in s:
    cyphered += chr(ord(i)^salt)

print("Шифрованная строка")
print(cyphered)


print("Расшифрованная строка")
s = ""
for i in cyphered:
    s += chr(ord(i)^salt)
print(s)