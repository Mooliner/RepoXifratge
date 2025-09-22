import random
import string
import json

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

alfabet = list(string.ascii_lowercase)
clau = alfabet.copy()
random.shuffle(clau)
substitucio = dict(zip(alfabet, clau))

def xifra_simple(text):
    resultat = []
    for c in text:
        if c in string.ascii_lowercase:
            resultat.append(substitucio[c])
        elif c in string.ascii_uppercase:
            resultat.append(substitucio[c.lower()].upper())
        else:
            resultat.append(c)
    return ''.join(resultat)

xifrat = xifra_simple(text)
print("Text xifrat (substitució simple):")
print(xifrat)
#with open("xifrat_simple.txt", "w", encoding="utf-8") as f:
#    f.write(xifrat)
print("Clau:")
print(substitucio)