
# a 
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# b
def euclides_extes(a, b):
    if b == 0:
        return a, 1, 0
    else:
        mcd, x1, y1 = euclides_extes(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return mcd, x, y

def invers_modular(a, n):
    mcd_val, x, y = euclides_extes(a, n)
    if mcd_val != 1:
        return None
    else:
        return x % n

# c
def exp_mod_bin(a, b, n):
    resultat = 1
    a = a % n
    while b > 0:
        if (b % 2) == 1:
            resultat = (resultat * a) % n
        b = b // 2
        a = (a * a) % n
    return resultat


#
# EXERCICI 2
#

# 1
p = 11
q = 17

print("p, q = ", p, q)

# 2
n = p * q
print(f"n = {n}")

# 3
phi_n = (p - 1) * (q - 1)
print(f"φ(n) = {phi_n}")

# 4
e = 7
print(f"e = {e}")

# 5
d = invers_modular(e, phi_n)
print(f"d = {d}")

# 6
print(f"Clau pública: (n, e) = ({n}, {e})")
print(f"Clau privada: (n, d) = ({n}, {d})")

# 7
m = 88
print(f"Missatge original: {m}")

# 8
c = exp_mod_bin(m, e, n)
print(f"c = m^e mod n = {c}")

# 9
m_desxifrat = exp_mod_bin(c, d, n)
print(f"m = c^d mod n = {m_desxifrat}")

# 10
if m == m_desxifrat:
    print("Missatge recuperat correctament!")
else:
    print("Error: el missatge no coincideix.")