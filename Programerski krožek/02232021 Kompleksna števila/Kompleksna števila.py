#dva nacina
#

import math

class Kompleksno:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
       return f"{self.x} + {self.y}i"
 
    def __add__(self, other):
        return Kompleksno(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Kompleksno(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __abs__(self):
       return (self.x * self.x + self.y * self.y)**0.5

    def __truediv__(self, other):
        ab = abs(other)**2
        return self * Kompleksno(other.x/ab, -other.y/ab)
    #naredi __sub__(self, other):


    #naredi neki z ulomki

    def kot(self):
        if self.x == 0 and self.y == 0:
            return 0
        return int(math.degrees(math.atan2(self.y, self.x)))



def sestej_stevili(a,b):
    return Kompleksno(a.x + b.x, a.y + b.y)

def zmnozi(a,b):
    #(x1 + y1i) * (x2 + y2i) = x1*x2 +x1y2i + x2y1i - y1y2 = (x1*x2 - y1*y2) + (x1y2 +x2y1)
    return Kompleksno(a.x * b.x + a.y * b.y, a.x * b.y + a.y * b.x)




a = Kompleksno(3,4)
b = Kompleksno(0,1)
c = Kompleksno(4,3)
d = a * c

print(d.kot())
a_kot = a.kot()
c_kot = c.kot()
print(a_kot + c_kot)

print(d.abs())
print(a.abs()*c.abs())

"""print(a)
print(b)
print(sestej_stevili(a,b))
print(zmnozi(a,b))
print(a+b)
"""
