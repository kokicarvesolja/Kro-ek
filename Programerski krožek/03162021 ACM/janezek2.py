import functools import lru_cache


import sys
f = open("03162021 ACM/janezek.in")

nizi = f.readline().split(",")
stevilke = []
for c in nizi:
    stevilke.append(int(c))
print(stevilke)


@lru_cache (maxsize = None)
def maksimum(mesto_janezka):
    if len(stevilke) - 1== mesto_janezka:
        return stevilke[mesto_janezka]
    if mesto_janezka >= len(stevilke):
        return 0
    
    #izberemo
    prva_moznost = stevilke[mesto_janezka] + maksimum(mesto_janezka + 2)
    # ne izberemo
    druga_moznost = maksimum(mesto_janezka + 1)

    return max(prva_moznost, druga_moznost)
