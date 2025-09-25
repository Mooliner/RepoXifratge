import re
from collections import Counter, defaultdict

with open("text.txt", "r", encoding="utf-8") as f:
    ciphertext = f.read()

def clean_text(text):
    return re.sub('[^a-zA-Z]', '', text).lower()

def friedman_ic(text):
    N = len(text)
    freqs = Counter(text)
    ic = sum(f*(f-1) for f in freqs.values()) / (N*(N-1)) if N > 1 else 0
    k_est = (0.027 * N) / ((N - 1) * ic - 0.038 * N + 0.065) if ic > 0 else None
    return ic, k_est

def kasiski_candidates(text, min_size=3, max_size=5, max_key=30):
    positions = defaultdict(list)
    for size in range(min_size, max_size+1):
        for i in range(len(text) - size + 1):
            seq = text[i:i+size]
            positions[seq].append(i)
    distances = []
    for seq, poslist in positions.items():
        if len(poslist) > 1:
            for i in range(len(poslist)-1):
                for j in range(i+1, len(poslist)):
                    distances.append(poslist[j] - poslist[i])
    divcount = Counter()
    for d in distances:
        for k in range(2, max_key+1):
            if d % k == 0:
                divcount[k] += 1
    return divcount.most_common()

catalan_freq = {
 'a':0.115,'b':0.012,'c':0.040,'d':0.046,'e':0.133,'f':0.010,
 'g':0.009,'h':0.007,'i':0.070,'j':0.006,'k':0.000,'l':0.060,
 'm':0.030,'n':0.067,'o':0.058,'p':0.031,'q':0.011,'r':0.065,
 's':0.079,'t':0.060,'u':0.046,'v':0.021,'w':0.000,'x':0.003,
 'y':0.001,'z':0.001
}

def chi_squared_stat(counter, expected, length):
    chi = 0.0
    for ch in expected:
        obs = counter.get(ch, 0)
        exp = expected[ch] * length
        if exp > 0:
            chi += (obs - exp)**2 / exp
    return chi

def guess_key_by_chi(text, keylen, expected=catalan_freq):
    cols = [text[i::keylen] for i in range(keylen)]
    key = ''
    shifts = []
    for col in cols:
        best_shift = None
        best_chi = float('inf')
        for s in range(26):
            dec = ''.join(chr((ord(c)-97 - s) % 26 + 97) for c in col)
            cnt = Counter(dec)
            chi = chi_squared_stat(cnt, expected, len(dec))
            if chi < best_chi:
                best_chi = chi
                best_shift = s
        key += chr(97 + best_shift)
        shifts.append(best_chi)
    return key, sum(shifts)/len(shifts)

def minimal_period(s):
    """Redueix una clau repetida a la seva forma mínima."""
    n = len(s)
    for p in range(1, n+1):
        if n % p == 0 and s == s[:p] * (n // p):
            return s[:p]
    return s

def decrypt_preserve(text, key):
    res = []
    klen = len(key)
    ki = 0
    for ch in text:
        if ch.isalpha():
            k = ord(key[ki % klen].lower()) - 97
            base = ord('A') if ch.isupper() else ord('a')
            res.append(chr((ord(ch) - base - k) % 26 + base))
            ki += 1
        else:
            res.append(ch)
    return ''.join(res)


def main():
    clean = clean_text(ciphertext)
    ic, k_est = friedman_ic(clean)
    print(f"[Friedman] IC = {ic:.6f}    estimació K ≈ {k_est:.2f}")
    kas = kasiski_candidates(clean, min_size=3, max_size=5, max_key=40)
    print("[Kasiski] top candidats (k, comptes):", kas[:12])

    candidates = sorted(set([k for k,_ in kas[:10] if 2 <= k <= 40] + list(range(2,13)) +
                            ([round(k_est)] if k_est else [])))

    seen_keys = set()
    results = []
    for k in candidates:
        key_guess, avg_chi = guess_key_by_chi(clean, k, catalan_freq)
        key_min = minimal_period(key_guess)
        if key_min in seen_keys:
            continue
        seen_keys.add(key_min)
        plain = decrypt_preserve(ciphertext, key_min)
        results.append((len(key_min), key_min, avg_chi, plain[:200]))

    results.sort(key=lambda x: x[2])
    print("\nClaus candidates (longitud mínima, clau, χ²):")
    for i,(k,key,chi,snip) in enumerate(results[:3],1):
        print(f"{i}. len={k:2d}  key='{key}'  avg_chi={chi:.2f}")
        print("   inici text:", snip.replace('\n',' '), "\n")

if __name__ == "__main__":
    main()
