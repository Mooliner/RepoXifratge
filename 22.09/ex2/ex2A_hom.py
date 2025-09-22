import random
import string
import json

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

alfabet = string.ascii_lowercase

homofons = {}
for l in alfabet:
    freq_bonus = {'e':4, 'a':3, 'o':3, 's':2, 'n':2}
    n_simbols = freq_bonus.get(l, 1)      
    codes = []

    for i in range(n_simbols):
        if i % 2 == 0: 
            codes.append(''.join(random.choices(string.ascii_uppercase, k=2)))
        else: 
            codes.append(str(random.randint(100,999)))
    homofons[l] = codes


def xifra_homofon(text):
    resultat = []
    for c in text:
        cl = c.lower()
        if cl in homofons:
            resultat.append(random.choice(homofons[cl]))
        else:
            resultat.append(c)   
    return ' '.join(resultat) 


xifrat = xifra_homofon(text)
print("Text xifrat (substitució homòfon):")
print(xifrat)
#with open("xifrat_homofon.txt", "w", encoding="utf-8") as f:
#    f.write(xifrat)
print("Clau:")
print(json.dumps(homofons, indent=2))
