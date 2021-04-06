# Napiši program, ki sešteje in zmnoži vse člene v seznamu, nato pa izpiše še minimum in maksimum seznama. 

seznam = [3, 1, 10, 2, 4, 9, 5, 8, 6, 7, -1, -3, 100]

vsota_stevil = 0
zmnozek_stevil = 1
max_stevilo = seznam[0]
min_stevilo = seznam[0]

for i in range(len(seznam)):
    vsota_stevil += seznam[i]
    zmnozek_stevil *= seznam[i]
    if max_stevilo < seznam[i]:
        max_stevilo = seznam[i]
    if min_stevilo > seznam[i]:
        min_stevilo = seznam[i]

print(vsota_stevil)
print(zmnozek_stevil)
print(min_stevilo)
print(max_stevilo)


