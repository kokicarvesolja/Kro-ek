ime_uporabnika = input("Kako ti je ime? ")
starost_uporabnika = int(input("Koliko si star?"))
starost_letnica = int(input("Za katero leto bi rad vedel, koliko boš star? "))

print("Pozdravljen, ", ime_uporabnika)
print("Rojen si bil ", 2021 - starost_uporabnika)
print("Star si ", starost_uporabnika)
print("Čez 10 let boš star ", starost_uporabnika + 10)
print("Leta ", starost_letnica, " boš star ", (starost_letnica - 2021) + starost_uporabnika , " let.")