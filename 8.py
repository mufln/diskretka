import re
from string import ascii_lowercase
alph = ascii_lowercase

def caesar(s, k):
    return ''.join([ascii_lowercase[(ascii_lowercase.index(c) + k) % 26] for c in s])


alphabetFrequency = ['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p'
                     'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q']

s = "On another occasion, while staying with Wilde in Brighton, Douglas fell ill with influenza and was nursed by Wilde, but failed to return the favour when Wilde himself fell ill having caught influenza in consequence. Instead Douglas moved to the luxurious Grand Hotel and on Wilde's 40th birthday sent him a letter informing him that he had charged Wilde with the hotel bill. Douglas also gave his old clothes to male prostitutes, but failed to remove from the pockets incriminating letters exchanged between him and Wilde, which were then used for blackmail.[14]"
s = s.lower()
s = re.sub('[^a-z]','',s)
t = caesar(s,3)



def deCaesar(t):
    t = t.lower()
    count = [0]*26
    for i in t:
        if i in alph:
            count[alph.index(i)]+=1
    shift = -(ord(alph[count.index(max(count))])-ord(alphabetFrequency[0]))
    return caesar(t,shift)

print(deCaesar(t))