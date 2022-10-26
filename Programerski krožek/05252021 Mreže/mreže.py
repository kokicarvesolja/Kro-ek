import random

random.seed(2021)

mreza = [ 
    [0,0,1,1], 
    [1,1,0,0]
]

def prazna_mreza(y, x):
    PraznaMreza = []
    Vstavljanje = []
    for _ in range(x):
        Vstavljanje.append(0)
    for _ in range (y):
        PraznaMreza.append(Vstavljanje[:])
    return PraznaMreza

def izpisi_mrezo(mreza):
    dolzina_mreze = len(mreza)
    dolzina_seznama = len(mreza[0])
    for j in range(dolzina_mreze):
        for i in range(dolzina_seznama):
            if mreza[j][i] == 1:
                if i == (dolzina_seznama - 1):
                    print("#")
                else:
                    print("#", end="")
            elif mreza[j][i] == 0:
                if i == (dolzina_seznama - 1):
                    print(".")
                else:
                    print(".", end="")
            elif mreza[j][i] == -1:
                if i == (dolzina_seznama - 1):
                    print("P")
                else:
                    print("P", end="")


def nakljucno_napolni (mreza, p):
    dolzina_mreze = len(mreza)
    dolzina_seznama = len(mreza[0])
    for j in range(dolzina_mreze):
        for i in range(dolzina_seznama):
            random_stevilo = random.random()
            if random_stevilo < p:
                mreza[j][i] = 0
            else:
                mreza[j][i] = 1
    return mreza

simba = -1

def flood_fill_bla (mreza, j, i, simbol):
    print(mreza, "nova")
    mreza[j][i] = -1
    if i < len(mreza[0]) -1: #preveri desnega
        if mreza[j][i + 1] == 0:
            flood_fill_bla(mreza, j, i + 1, simbol)
    elif i >= len(mreza[0]) - 1:
        i += 1 - len(mreza[0])
        if mreza[j][i] == 0:
            flood_fill_bla(mreza, j, i + 1, simbol)

    if i > 0: #preveri levega
        if mreza[j][i -1] == 0:
            flood_fill_bla(mreza, j, i -1, simbol)
    elif i <= 0:
        i -= 1 + len(mreza)
        if mreza[j][i] == 0:
            flood_fill_bla(mreza, j, i - 1, simbol)

    if j < len(mreza) - 1: #preveri zgornjega
        if mreza[j + 1][i] == 0:
            flood_fill_bla(mreza, j + 1, i, simbol)
    elif j >= len(mreza) - 1:
        j += 1 - len(mreza)
        if mreza[j][i] == 0:
            flood_fill_bla(mreza, j + 1, i, simbol)

    if j > 0: #preveri spodnjega
        if mreza[j - 1][i] == 0:
            flood_fill_bla(mreza, j - 1, i, simbol)
    elif j <= 0:
        j -= 1 + len(mreza)
        if mreza[j][i] == 0:
            flood_fill_bla(mreza, j - 1, i, simbol)
    pass

def flood_fill(mreza, j, i, simbol):
    print(mreza)

    if i >= len(mreza[0]):
        i = 0
    elif i < 0:
        i = len(mreza[0]) - 1
    elif j >= len(mreza):
        j = 0
    elif j < 0: 
        j = len(mreza) - 1
    
    if mreza[j][i] == 0:
        mreza[j][i] = -1
    if mreza[j][i] == 1 or mreza[j][i] == -1: 
        pass
    
    flood_fill(mreza, j, i + 1, simbol) #desni
    flood_fill(mreza, j, i - 1, simbol) #levi
    flood_fill(mreza, j + 1, i, simbol)  # zgornji
    flood_fill(mreza, j - 1, i, simbol) # spodnji

    
flood_fill(nakljucno_napolni(prazna_mreza(4,4), 0.5), 1, 1, simba)  

            


