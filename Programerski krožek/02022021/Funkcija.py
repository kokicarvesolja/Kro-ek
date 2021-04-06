# Napišemo funkcijo za fakulteto

def izracunaj_fakulteto(stevilo):
    zmnozek_fakultete = 1

    for i in range(1, stevilo + 1):
        zmnozek_fakultete *= i
        
    return (zmnozek_fakultete)



def sestevanje_stevk(stevilo1):  
    string_zmnozka = str(stevilo1)
    vsota_stevil = 0

    for i in range(len(string_zmnozka)):
        vsota_stevil += int(string_zmnozka[i])
    
    return(vsota_stevil)


f_5 = izracunaj_fakulteto(5)
f5vsota = sestevanje_stevk(f_5)

print(f_5)
print(f5vsota)

f_10 = izracunaj_fakulteto(10)
f10vsota = sestevanje_stevk(f_10)

print(f_10)
print(f10vsota)