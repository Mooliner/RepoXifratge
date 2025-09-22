import string

text = """
T SLGP DPPY ESTYRD JZF APZAWP HZFWO YZE MPWTPGP, LEELNV DSTAD
ZY QTCP ZQQ ESP DSZFWOPC ZQ ZCTZY, T HLENSPO N-MPLXD RWTEEPC
TY ESP OLCV YPLC ESP ELYYSLFDPC RLEP. LWW ESZDP XZXPYED HTWW
MP WZDE TY ETXP, WTVP EPLCD TY CLTY. ETXP EZ OTP.
"""

def desxifrat_cesar(text, clau):
    resultat = []
    for c in text:
        if c in string.ascii_uppercase:
            nou_c = chr((ord(c) - ord('A') - clau) % 26 + ord('A'))
            resultat.append(nou_c)
        else:
            resultat.append(c)
    return ''.join(resultat)

for clau in range(26):
    print(f"Clau {clau}:")
    print(desxifrat_cesar(text, clau))  