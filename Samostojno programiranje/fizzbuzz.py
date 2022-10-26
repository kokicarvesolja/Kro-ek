import time

def fizzbuzz (stevilo):
    for i in range(stevilo + 1):
        if i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 5 == 0 and i % 3 != 0: 
            print("buzz")
        elif i % 5 == 0 and i % 3 == 0:
            print("Fizzbuzz")
        else: 
            print(i)

Fizzbuzz_stevilo = int(input("Vnesi število: "))

print(fizzbuzz(Fizzbuzz_stevilo))

