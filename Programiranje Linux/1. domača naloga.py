# program uporabnika povpraša po mesecu in po letu
# mesec: 2 seznama, enega za 30 dni in drugega za 31 dni ter posebej februar
# leto: če je pri deljenju ostanek 0, potem je prestopno leto, in je februar 29 dni

meseci_31dni = [1,3,5,7,8,10,12]
meseci_30dni = [4,6,9,11]

milis_dan = 60*60*24*1000

milis_mesec = 0

potrditev = 0

while potrditev == 0:
    uporabnikov_mesec= int(input("Milisekund v katerem mesecu: "))
    uporab_leto = int(input("Izbrano leto za mesec: "))
    print("Zanimajo te milisekunde za ", uporabnikov_mesec, ". mesec leta ", uporab_leto, "?")
    potrditev = int(input("0 = nisem zadovoljen z izbiro, 1 = nadaljuj: "))

if uporabnikov_mesec in meseci_30dni:
    milis_mesec = milis_dan*30
elif uporabnikov_mesec in meseci_31dni:
    milis_mesec = milis_dan * 31
elif uporabnikov_mesec > 12: 
    print("Ni toliko mesecev, butec.")
else:
    if uporab_leto%4 == 0 and (uporab_leto%100 != 0 or uporab_leto%400 == 0):  # pomagal Google
        milis_mesec = milis_dan * 29
    else:
        milis_mesec = milis_dan * 28

print("Milisekund v ", uporabnikov_mesec, ". mesecu leta ", uporab_leto, "je: ", milis_mesec)