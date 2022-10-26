# Napiši program, ki od uporabnika dobi naravno število n, nato pa nariše "smrekico" iz zvezdic. 
# Smrekica naj ima n vrstic. 

n = int(input("Naravno število n: ")) +1
i = 1

for i in range(n):
    print(i*"*")
    i += 1

for i in range(n):
    n -= 1
    print(n*" ",i*"*")
    i += 1