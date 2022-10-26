import time

def najdi (sez, x):
    for i in range(len(sez)):
        if sez[i] == x:
            return i
    return - 1

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 24, 50, 100]
y = 24

seznam_do_100 = []

for i in range(100):
    seznam_do_100.append(i + 1)

def najdi_pametno (sez, x):
    for i in range(len(sez)):
        if sez[i] <= x:
            if sez[i] == x:
                return i
    return -1

def bisekcija(sez, x, levi, desni):
    polovica = (levi + desni) // 2
    if sez[polovica] == x:
        return polovica
    if len(sez) == 1 and sez[polovica] != x: 
        return -1
    if x < sez[polovica]:
        return bisekcija (sez, x, levi, polovica)
    if x > sez[polovica]:
        return bisekcija (sez, x, levi + 1, desni)

#print(bisekcija(seznam_do_100, y, 0, len(seznam_do_100)))

print('First line \n Second line') 
    
