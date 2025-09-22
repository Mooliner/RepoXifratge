from collections import Counter
import string

text = """
T SLGP DPPY ESTYRD JZF APZAWP HZFWO YZE MPWTPGP, LEELNV DSTAD
ZY QTCP ZQQ ESP DSZFWOPC ZQ ZCTZY, T HLENSPO N-MPLXD RWTEEPC
TY ESP OLCV YPLC ESP ELYYSLFDPC RLEP. LWW ESZDP XZXPYED HTWW
MP WZDE TY ETXP, WTVP EPLCD TY CLTY. ETXP EZ OTP.
"""

# Només lletres majúscules
lletres = [c for c in text if c in string.ascii_uppercase]
freq = Counter(lletres)

total = sum(freq.values())
for lletres, count in freq.most_common():
    print(f"{lletres}: {count}")