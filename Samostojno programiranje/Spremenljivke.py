# popolni kvadrati
import math
x = int(input("Vpiši celo število: "))
y= math.sqrt(x) #koren
yint = int(y) # pretvori možno float število v int število
if yint == y: 
    print(y)
else:
    print("Izberi si drugo število, kreten.")
