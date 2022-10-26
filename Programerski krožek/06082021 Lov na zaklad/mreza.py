import random

def seed():
    random.seed(2021)

def prazna_mreza(w, h):
    return [
        [0 for j in range(w)] for _ in range(h)
    ]

def cell(a):
    if a == 0:
        return "."
    if a == 1:
        return "#"
    if a == 2:
        return "X"
    if a == 3: 
        return "0"

def print_mreza(m):
    rr = "\n".join(
        "".join([cell(x) for x in l]) for l in m
    )
    return rr

def random_mreza(m, p1, p2, p3):
    seed()
    for j in range(len(m)):
        v = m[j]
        for i in range(len(v)):
            r = random.random()
            n = 3
            if r < p1:
                n = 0
            elif r < p2:
                n = 1
            elif r < p3:
                n = 2
            v[i] = n
    return m




p1 = 0.7
p2 = 0.8
p3 = 0.9
mreza = prazna_mreza(200, 150)
#print(print_mreza(mreza))
random_mreza(mreza, p1, p2, p3)
#print(print_mreza(mreza))

kolicina_helija = 0
denar = 0

for j in range(len(mreza)):
    for i in range(len(mreza[j])):
        if mreza[i][j] == 1:
            kolicina_helija += 1

#print(kolicina_helija)

denar = kolicina_helija*12

#print(denar)

stevilo_skal = 0

for j in range(len(mreza)):
    for i in range(len(mreza[j])):
        if mreza[j][i] == 2:
            stevilo_skal += 1

#print(stevilo_skal)

denar_po_skalah= denar - stevilo_skal*4

#print(denar_po_skalah)

izbran_stolpec = 0

helij = 0
skale = 0
nev_plin = 0
bla = []

for i in range(len(mreza[0])):
    for j in range(len(mreza)):
        if mreza[j][i] == 1:
            helij += 1
        elif mreza[j][i] == 2:
            skale += 2
        elif mreza[j][i]== 3:
            nev_plin += 1
        kolicina_denarja = helij*12 - skale*4 - nev_plin*6
        bla.append(kolicina_denarja)

        
#print(bla.index(max(bla)))



            