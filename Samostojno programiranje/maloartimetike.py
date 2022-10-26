# Napiši program, ki od uporabnika prebere število n, in izpiše vsoto vseh naravnih števil do vključno n, ter produkt vseh
# naravnih števil do vključno n.

uporabnikovo_stevilo = int(input("Vnesi število: "))

i = 1
zmnozek_stevil = 1

vsota_stevil = (uporabnikovo_stevilo * (1 + uporabnikovo_stevilo))/2
for i in range(1, uporabnikovo_stevilo + 1):
    zmnozek_stevil = zmnozek_stevil * i
     
print("Vsota vseh števil do ", uporabnikovo_stevilo, "je: ", vsota_stevil)
print("Zmnožek vseh števil do ", uporabnikovo_stevilo, "je: ", zmnozek_stevil)