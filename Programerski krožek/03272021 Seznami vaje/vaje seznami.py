# vaje seznami
# Sestavi funkcijo `razpolovi_seznam`, ki seznam prepolovi 
# na dva podseznama in ju vrne kot par seznamov. 
# V primeru lihe dolžine naj bo dolžina prvega podseznama 
# krajša ali enaka dolžini drugega podseznama.
#    razpolovi_seznam([5, 4, 3, 2, 1])
#    ([5, 4], [3, 2, 1])

# Sestavi funkcijo zdruzi sezname, ki sprejme seznam seznamo in jih združi v en sam seznam:
# >>> zdruzi_sezname([[1], [2, 3], [4, 5, 6]])
# [1, 2, 3, 4, 5, 6]
# >>> zdruzi_sezname([[], [0], [], [0], [], [7], []])
# [0, 0, 7]

# Sestavi funkcijo porezani_podseznami, ki sprejme seznam in zgradi nov seznam podseznamov, 
# ki jih pridobimo tako, da podanemu seznamu po vrsti odstranjujemo začetne elemente.

# >>> porezani_podseznami([1, 2, 3, 4])
# [[1, 2, 3, 4], [2, 3, 4], [3, 4], [4], []]

def razpolovi_seznam(seznam):
    dolzina_seznama = int(len(seznam)/2)
    prvi_seznam =[]
    drugi_seznam = []
    for i in range(len(seznam)):
        if i < dolzina_seznama:
            prvi_seznam.append(seznam[i])
        elif i >= dolzina_seznama:
            drugi_seznam.append(seznam[i])
    return prvi_seznam, drugi_seznam
    
seznam_1 = [6 ,5, 4, 3, 2, 1]

prva_groza, druga_groza = razpolovi_seznam(seznam_1) #seznam da na dva dela

# print(prva_groza, druga_groza)

negativa = [0, -1, -2] #tretji seznam


def zdruzi_sezname (seznam): #sprejme en seznam seznamov in ga da v skupen seznam
    skupen_seznam = []
    for i in range(len(seznam)):
       for j in range(len(seznam[i])):
           skupen_seznam.append(seznam[i][j])
    return skupen_seznam

def porezani_podseznami (seznam):
    podseznam = []
    

print(porezani_podseznami(seznam_1))
