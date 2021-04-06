class Kompleksno:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "+" + str(self.y) + "i"
    
def sestej_stevili(a,b):
    return Kompleksno(a.x + b.x, a.y + b.y)

def zmnozi(a,b):
    return Kompleksno(a.x*b.x - a.y*b.y, a.x*b.y + a.y*b.x)

a = Kompleksno(3,4) # 3 + 4i
b = Kompleksno (0, 1) # 0 + 1i

print(a)
print(b)
print(sestej_stevili(a,b))
print(zmnozi(a,b))