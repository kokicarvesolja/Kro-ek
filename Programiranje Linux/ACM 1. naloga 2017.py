# število, ki ima decimalko 0,5 ali več se zaokroži navzgor, manj od tega se zaokroži navzdol 
# isto s temperaturami z negativnimi predznaki
# Število, ki je med vključno z -0,5 in izključno 0, se zaokroži v -0 


def najbidelalo(x,y): 
    if (-0.5)<= x and x < 0:
        x = -0
    else:
        y = (x - int(x))
        if 0.0 <= y and y < 0.4:
            x = int(x)
        elif 0.5 <= y and y <= 0.9:
            x = int(x) + 1
        elif (-0.5) <= y and y <= 0.0:
            x = int(x) 
        elif (-0.9) <= y and y < (-0.5):
            x = int(x) -1
    return

vnesena_temperatura = float(input("Vnesi število: "))