import math


SECONDS_PER_YEAR = 31_557_600      # segons en un any
RATE = 1e9                         # velocitat de l'ordinador potent: 10^9 claus/s

def time_years(keys):
    """Retorna el temps en anys (pitjor cas) amb RATE = 1e9 claus/s"""
    return keys / RATE / SECONDS_PER_YEAR

# (a) 
substitution_keys = math.factorial(26)
print("=== Ordinador potent (1e9 claus/s) ===")
print(f"(a) Substitució 26!: {time_years(substitution_keys):.2e} anys")

# (b)
permutation_keys = math.factorial(10)
print(f"(b) Permutació 10!:  {permutation_keys / RATE:.4f} segons")

# (c)
def vigenere_keys(k): return 26 ** k
for k in [4, 6, 8, 10, 12]:
    t_sec = vigenere_keys(k) / RATE
    if t_sec < 3600:
        print(f"(c) Vigenère k={k}: {t_sec:.2f} s")
    elif t_sec < 86_400:
        print(f"(c) Vigenère k={k}: {t_sec/3600:.2f} h")
    else:
        print(f"(c) Vigenère k={k}: {t_sec/86_400:.2f} dies")
