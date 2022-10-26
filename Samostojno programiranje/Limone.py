x = int(input("Vnesi številko in povedal ti bom, koliko limon ti bo dalo življene: "))

y = str(x)

z = len(y)

if z == 1 or int(y[-2]) == 0:
    if int(y[-1]) == 1: #za številko, ki se konča z 1, se izpiše, da imaš 1 limono
        print("Imaš ", x, " limono.")
    elif int(y[-1]) == 2: # 2 limoni
        print("Imaš ", x, " limoni.")
    elif int(y[-1]) == 3 or int(y[-1]) == 4: # 3 limone + rad bi tudi, da je 4 tudi zraven
        print("Imaš ", x, " limone.")
    else:
        print("Imaš ", x, " limon.")
else:
    print("Imaš ", x, " limon.")