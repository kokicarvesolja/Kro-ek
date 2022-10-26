# Napiši program, ki od uporabnika prebere število n, in izpiše vsoto vseh naravnih števil do vključno n, ter produkt vseh
# naravnih števil do vključno n.

uporabnikovo_stevilo = int(input("Vnesi število: "))

vsota_stevil=0
i = 0
zmnozek_stevil = 1

for i in range(1, uporabnikovo_stevilo + 1):
    vsota_stevil = vsota_stevil + i
    zmnozek_stevil = zmnozek_stevil*i

print(vsota_stevil)
print(zmnozek_stevil)