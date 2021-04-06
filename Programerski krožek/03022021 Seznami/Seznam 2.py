# Napiši funkcijo minimum, maximum, vsota, produkt
# Dobijo seznam in vrnejo 
# Funkcija fakulteta ki dobi seznam števil in vrne seznam fakultet števil
# [1, 5, 8, 3] -> [1!, 5!, 8!, 3!]

seznam = [1, 5, 8, 4, 10, 15, 26, -3]

def minimum (seznama):
    return min(seznama)


def maksimum (seznama):
    return max(seznama)

def vsota (seznama):
    vsota_seznama = 0
    for i in range(len(seznama)):
        vsota_seznama += seznama[i]
    return vsota_seznama

def produkt (seznama):
    produkt_seznama = 1
    for i in range(len(seznama)):
        produkt_seznama *= seznama[i]
    return produkt_seznama

def fakulteta(x):
    produkt_fakultete = 1
    for i in range(x):
        produkt_fakultete *= (i+1)
    return produkt_fakultete

def seznam_fakultet(seznama):
    fakultete = []
    for i in range(len(seznama)):
        fakultete.append(fakulteta(seznama[i]))
    return fakultete


print(seznam_fakultet(seznam))
