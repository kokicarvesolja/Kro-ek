dolzina = int(input("Vnesi število, ... bedak: "))

fakulteta = 1

zmnozek_fakultete = 1
vsota_stevil = 0

for i in range(dolzina):
    zmnozek_fakultete *= fakulteta
    fakulteta += 1

print(zmnozek_fakultete)

dolzina_rezultata = str(zmnozek_fakultete)
fakulteta = 0

for i in range(1,len(dolzina_rezultata)):
    vsota_stevil += int(dolzina_rezultata[fakulteta])
    fakulteta += 1

print(vsota_stevil)