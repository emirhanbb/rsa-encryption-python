print("Sending Word: ")
gonderilecekHarf = input()
p = 79
q = 67
n = p * q
totient = (p - 1) * (q - 1)
e = 7
d = (2 * totient + 1) / e
gonderilecekHarfSayisi = ord(gonderilecekHarf)
gonderenSifre = pow(gonderilecekHarfSayisi, e) % n
print("Gönderilen Şifre: ", gonderenSifre)
aliciSifre = pow(gonderenSifre, int(d)) % n
print("Çözülen Şifre: ", aliciSifre)
print("Bulunan Harf: ", chr(aliciSifre))
