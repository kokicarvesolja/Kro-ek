seznam_imen = ["Filip", "Miha", "Luka", "Martin", "Kristofer", "Maja", "Maja", "Maja"]

iskano_ime = "Maja"

index_imena = 0

ze_najdeno = True

while index_imena < len(seznam_imen) and ze_najdeno == True: 
    
    trenutno_ime = seznam_imen[index_imena]

    if trenutno_ime == iskano_ime:
        print("Našel sem ga, je na mestu ",index_imena)
        ze_najdeno = False
    
    index_imena += 1 