import math
import time

y = False

while y != True:
    x = int(input("Vnesi naključno celo število: "))
    xrt = math.sqrt(x) #koreni
    xint = int(xrt) #pretvori število v število brez decimalk
    if xint == xrt: 
        y = True
        print(xrt, """
        Bravo našel si popoln kvadrat.
        """)
    else: 
        y = False
        print("Poskusi še enkrat čez 1 sekundo.")
        time.sleep(1) #počakaš 1 sekundo preden greš lahko novo številko poskusiti. 