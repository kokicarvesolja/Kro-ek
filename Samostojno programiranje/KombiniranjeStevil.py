x = int(input("Vnesi število x: "))
y = int(input("Vnesi število y: "))
z = int(input("Vnesi število z: "))

if x+y == z:
    print(x, "+", y, "=", z)
elif z+y == x:
    print(x, "-", y, "=", z)
elif z + x == y:
    print(y, "-", x, "=", z)
elif y*x == z:
    print(x, "×", y, "=", z)
elif z*y == x:
    print(x, "/", y, "=", z)
elif z*x == y:
    print(y, "/", x, "=", z)
else: 
    print("Ni možne kombinacije števil", x, " in ", y, ", da dobimo število ", z, ".")