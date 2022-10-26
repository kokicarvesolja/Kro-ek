a="""
Vpiši. 
Naključno.
Število.
"""
print(a)
x = int(input("Tukaj: "))

i=0

while (i**2) <= x:
    if (i**2) == x:
        print("Tvoja številka je popoln kvadrat.")
        print(i)
        break
    else:
        i+=1