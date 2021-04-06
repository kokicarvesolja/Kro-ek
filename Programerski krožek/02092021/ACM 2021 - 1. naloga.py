vnos_uporabnika = "xoxoxo"

def izenaceno(niz):
    niz = str(niz)
    znak_x = 'x'
    kolicina_zap_x= 0
    znak_o = 'o'
    kolicina_zap_o = 0
    kolicina_x = 0
    kolicina_o = 0
    for i in range(len(niz)):

        if znak_x == niz[i]:
            kolicina_zap_x+= 1
            kolicina_zap_o = 0
            kolicina_x += 1
            if kolicina_zap_x>= 3:
                print("Zmagal je igralec z x-i.")
                return

        elif znak_o == niz[i]:
            kolicina_zap_o += 1
            kolicina_zap_x= 0
            kolicina_o += 1
            if kolicina_zap_o >= 3:
                print("Zmagal je igralec z o-ji.")
                return

        elif niz[i] != znak_o and niz[i] != znak_x:
            print("Neveljaven znak.")
            return
    
    if kolicina_x == kolicina_o:
        print("Izenačeno.")
    else: 
        print("Ni izenačeno")
    
    return niz

izenaceno(vnos_uporabnika)