seznam_ni_po_vrsti = [1, 4, 5, 10, 8, 6]
seznam_je_po_vrsti = [1,2,3,4,5,6]

def seznam_po_vrsti (seznam):
    for i in range(len(seznam) - 1):
        if seznam[i] >= seznam[i + 1]:
            return ("Seznam ni po vrsti.")
    return "Seznam je po vrsti. "

print (seznam_po_vrsti(seznam_je_po_vrsti))