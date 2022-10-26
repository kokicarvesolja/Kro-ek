#Napiši program, ki od uporabnika prebere število n, nato pa izpiše po vrsti vse kvadrate naravnih števil do (vključno z) n.

uporabnikovo_stevilo = int(input("Vnesi število: "))

i = 0

while (i**2)<= uporabnikovo_stevilo:
    print(i**2)
    i += 1