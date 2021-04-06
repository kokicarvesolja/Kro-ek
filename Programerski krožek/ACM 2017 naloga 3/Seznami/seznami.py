# Sprašuje uporabnika po številkah in jih dodaja v seznam 

seznam_stevil = []

uporabnikovo_stevilo = int(input("Vnesi število: "))

while uporabnikovo_stevilo != 0:
    seznam_stevil.append(uporabnikovo_stevilo)
    uporabnikovo_stevilo = int(input("Vnesi število: "))

print("Vpisal si števila: ", seznam_stevil)

