#Sestavi program, ki izpiše prvih n členov Fibonaccijevega zaporedja. 
#To je zaporedje, podano s predpisom f1=1,f2=1,fn=fn−1+fn−2.

def fibonaccijeva_stevila(stevilo):
    fibonacci = 1
    fibonacci_1 = 1
    zaporedje_fibonacci = []
    zaporedje_fibonacci.append(fibonacci_1)
    for i in range(stevilo - 1):
        zaporedje_fibonacci.append(fibonacci)
        fibonacci = fibonacci + fibonacci_1
        fibonacci_1 = fibonacci - fibonacci_1
    return zaporedje_fibonacci


uporabnikovo_stevilo = int(input("Vnesi število členov Fibonaccijevega zaporedja: "))

f5 = fibonaccijeva_stevila(uporabnikovo_stevilo)

print(f5)