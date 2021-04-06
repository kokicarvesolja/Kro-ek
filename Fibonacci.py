#Sestavi program, ki izpiše prvih n členov Fibonaccijevega zaporedja. 
#To je zaporedje, podano s predpisom f1=1,f2=1,fn=fn−1+fn−2.

def fibonaccijeva_stevila(stevilo):
    fibonacci = 1
    fibonacci_1 = 1
    for i in range(1, stevilo + 1):
        fibonacci = fibonacci + fibonacci_1
        fibonacci_1 = fibonacci - fibonacci_1
    return fibonacci

 # uporabnikovo_stevilo = int(input("Vnesi število členov Fibonaccijevega zaporedja: "))

f5 = fibonaccijeva_stevila(30)

print(f5)