#Napiši program, ki od uporabnika bere števila, dokler uporabnik ne vpiše števila 0. Program naj sproti izpisuje največje, najmanjše in povprečje števil, vpisanih do sedaj.

vnos_uporabnika = 1
stevilo_vnosov = 0
sestevek_vnosov = 0
povprecje = 0
najvecje_stevilo = 0
najmanjse_stevilo = 0

while vnos_uporabnika != 0:
    vnos_uporabnika = int(input("Vnesi število: "))
    while najmanjse_stevilo == 0:
        najmanjse_stevilo = vnos_uporabnika
    while najvecje_stevilo == 0:
        najvecje_stevilo = vnos_uporabnika
    stevilo_vnosov +=1
    sestevek_vnosov += vnos_uporabnika
    povprecje = sestevek_vnosov/stevilo_vnosov
    if vnos_uporabnika > najvecje_stevilo:
        najvecje_stevilo = vnos_uporabnika
    elif vnos_uporabnika < najmanjse_stevilo:
        najmanjse_stevilo = vnos_uporabnika
    print (najmanjse_stevilo," ", povprecje, " ", najvecje_stevilo)