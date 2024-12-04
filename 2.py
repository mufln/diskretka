from collections import defaultdict
from math import log2

# Написать программу,
# чтобы провести статистическую обработку текста.

# Определить энтропию, приходящуюся в среднем на одну букву,
# длину кода при равномерном кодировании и избыточность.

# Построить схему алфавитного кодирования
# для однобуквенных сочетаний методом Шеннона-Фано.

# Найти среднюю длину элементарного кода,
# эффективность сжатия. Закодировать текст. Декодировать текст.

# Построить схему алфавитного кодирования для двухбуквенных
# сочетаний методом Шеннона-Фано. Найти среднюю длину элементарного кода,
# эффективность сжатия, сравнить с результатами для однобуквенных сочетаний.
# Закодировать текст. Декодировать текст.


s = "12342334551233"

stats = defaultdict(int)
two = defaultdict(int)
total = len(s)
for i in range(len(s)):
    if stats[s[i]]:
        stats[s[i]] += 1
    else:
        stats[s[i]] = 1
    if i + 1 >= len(s): continue
    k = s[i] + s[i + 1]
    if two[k]:
        two[k] += 1
    else:
        two[k] = 1

print("Колво символов в тексте")
print("     ", stats)
print("     ", two)
print('\nдлина текста - ', end='')
print(total)
entropy1 = {i: stats[i] / total for i in stats}
e1 = -sum([i * log2(i) for i in entropy1.values()])
print(f'энтропия для одной буквы {e1}')

entropy2 = {i: two[i] / total for i in two}
e2 = -sum([i * log2(i) for i in entropy2.values()])
print(f'энтропия для двух букв {-sum([i * log2(i) for i in entropy2.values()])}')

tuples1 = sorted(entropy1.items(), key=lambda x: x[1], reverse=True)
print("\n1 буквенные сочетания в порядке убывания частоты")
print("     ", tuples1)

tuples2 = sorted(entropy2.items(), key=lambda x: x[1], reverse=True)
print("\n2 буквенные сочетания в порядке убывания частоты")
print("     ", tuples2)

# храним коды
codes1 = defaultdict(str)
codes2 = defaultdict(str)


# шеннон-фано itself
def shannon(l, codes):
    g1 = []
    g2 = []
    group_by = sum(tuple[1] for tuple in l) / 2
    i = 0
    for tuple in l:
        if i < group_by:
            g1.append(tuple)
            if codes[tuple[0]]:
                codes[tuple[0]] += "0"
            else:
                codes[tuple[0]] = "0"
        else:
            g2.append(tuple)
            if codes[tuple[0]]:
                codes[tuple[0]] += "1"
            else:
                codes[tuple[0]] = "1"
        i += tuple[1]

    if len(g1) != 1:
        shannon(g1, codes)
    if len(g2) != 1:
        shannon(g2, codes)


shannon(tuples1, codes1)
shannon(tuples2, codes2)

l1 = sum([stats[i] * len(codes1[i]) for i in stats.keys()]) / total
print("\nКоды однобуквенных сочетаний")
print(codes1)
print(f"средняя длина элементарного кода для однобуквенных сочетаний {l1}")
efficiency1 = e1 / l1
print("эффективность сжатия для однобуквенных сочетаний ", efficiency1)

l2 = sum([two[i] * len(codes2[i]) for i in two.keys()]) / total
print("\nКоды двубуквенных сочетаний")
print(codes2)
print(f"средняя длина элементарного кода для двухбуквенных сочетаний {l2}")
efficiency2 = e2 / l1
print("эффективность сжатия для двухбуквенных сочетаний ", efficiency2)

decodes1 = {codes1[i]: i for i in codes1.keys()}
decodes2 = {codes2[i]: i for i in codes2.keys()}


def encode(s, codes):
    res = ""
    for i in s:
        if codes[i]:
            res += codes[i]
    return res


def encode2(s, codes):
    res = ""
    subs = ""
    i = 0
    keys = list(codes.keys())
    while (i < len(s)):
        while (not subs in keys):
            subs += s[i]
            i += 1
        res += codes[subs]
        subs = ""
    return res


print("\nЗакодированный текст")
print(encode(s, codes1))
print(encode2(s, codes2))


def decode(s, codes):
    res = ""
    subs = ""
    i = 0
    keys = list(codes.keys())
    while (i < len(s)):
        while (not subs in keys):
            subs += s[i]
            i+=1
        res += codes[subs]
        subs = ""
    return res



print("\nДекодированный текст")
print(decode(encode(s, codes1), decodes1))
print(decode(encode2(s, codes2), decodes2))
