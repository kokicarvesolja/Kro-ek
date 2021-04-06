možni_palindrom = [1,2,3,4]

def je_palindrom(seznam):
    palindrom_seznama = []
    for i in range(len(seznam)):
        palindrom_seznama.append(seznam[-(i+1)])
    return palindrom_seznama

#if možni_palindrom == je_palindrom(možni_palindrom):
#    print("Je palindrom.")
#else:
#    print("Ni palindrom")

def vrsta(seznam):
    for i in range(len(seznam)-1):
        if seznam[i] >= seznam[i+1]:
            return "Ni po vrsti"
    return "Je po vrsti"

#print(vrsta(možni_palindrom))

def vrsta_ni(seznam):
    for i in range(len(seznam)-1):
        if seznam[i] >= seznam[i+1]:
            return "Ni po vrsti"
    return "Je po vrsti"