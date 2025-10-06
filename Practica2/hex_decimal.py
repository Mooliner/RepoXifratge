# Programa per convertir un valor hexadecimal (copiat d'OpenSSL) a decimal

# Enganxa aquí el text hexadecimal tal com surt d'OpenSSL:
hex_text = """
    5d:85:ce:ea:f6:49:e0:f4:d3:76:0c:74:6d:cf:4b:
    ff:1d:34:26:10:18:e6:66:f4:92:77:b9:6a:69:e0:
    c2:27:63:cd:a8:2e:c4:80:b2:6e:9c:ba:7b:57:23:
    a8:11:10:a1:11:31:d6:40:61:f6:94:ac:26:1d:25:
    cb:2a:2d:eb:33:97:29:a3:1c:13:7e:12:b6:3e:d2:
    87:6c:6e:b9:e8:6f:63:8e:b5:d3:b2:9a:08:ab:c3:
    aa:1e:ac:26:3e:a7:15:40:20:94:2c:81:f3:b6:01:
    ab:64:49:5a:93:8f:30:ac:ce:b8:22:2e:57:2b:c0:
    52:9a:d2:19:20:dd:0a:da
"""

# 1️⃣ Eliminem dos punts, espais i salts de línia
clean_hex = hex_text.replace(":", "").replace("\n", "").replace(" ", "")

# 2️⃣ Convertim l'hexadecimal net a decimal
decimal_value = int(clean_hex, 16)

# 3️⃣ Mostrem el resultat
print("\nHexadecimal net:")
print(clean_hex)
print("\nValor decimal:")
print(decimal_value)
