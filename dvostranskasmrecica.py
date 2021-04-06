# Napiši program, ki od uporabnika dobi naravno število n, nato pa nariše "smrekico" iz zvezdic. 
# Smrekica naj ima n vrstic. 

n = int(input("Naravno število n: ")) +1
i = 1
desna_stran = 0

for i in range(1, n):
    n -=1
    print(n*" ", i*"*" + desna_stran*"*")
    desna_stran += 1  #git commitam