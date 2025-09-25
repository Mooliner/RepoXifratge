from collections import Counter
import string

text = """
T SLGP DPPY ESTYRD JZF APZAWP HZFWO YZE MPWTPGP, LEELNV DSTAD
ZY QTCP ZQQ ESP DSZFWOPC ZQ ZCTZY, T HLENSPO N-MPLXD RWTEEPC
TY ESP OLCV YPLC ESP ELYYSLFDPC RLEP. LWW ESZDP XZXPYED HTWW
MP WZDE TY ETXP, WTVP EPLCD TY CLTY. ETXP EZ OTP.
"""


caracters = [c.lower() for c in text if c.lower() in string.ascii_lowercase or c in string.digits]
freq = Counter(caracters)

total = sum(freq.values())
for c, count in freq.most_common():
    print(f"{c}: {count}")
