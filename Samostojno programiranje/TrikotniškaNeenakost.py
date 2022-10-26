import math

def O(a,b,c):
    P = a + b + c
    return P

def ploščina(a,b,c):
    s = O(a,b,c)/2
    S = math.sqrt(s*(s-x)*(s-y)*(s-z))
    return S

print("Vnesi 3 stranice:")
x = float(input("Vnesi število x:"))
y = float(input("Vnesi število y:"))
z = float(input("Vnesi število z:"))

if x < y + z and y < x + z and z < y + x:
    print("Trikotnik obstaja.")
    print ("Njegov obseg je ", O(x,y,z))
    print ("Njegova ploščina je ", ploščina(x,y,z), " oz.", round(ploščina(x,y,z), 2))
else:
    print("Trikotnik ne obstaja")