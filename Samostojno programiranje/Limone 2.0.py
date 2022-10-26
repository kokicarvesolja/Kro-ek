x = int(input("Vnesi številko in povedal ti bom, koliko limon ti bo dalo življene: "))

y = x % 10

if x % 100 <= 4:
    if y == 1:
        print("Imaš ", x, " limono.")
    elif y == 2:
        print("Imaš ", x, " limoni.")
    elif y == 3 or y == 4:
        print("Imaš ", x, " limone.")
else:
    print("Imaš ", x, " limon.")