seznam = [1,2,3,4,5,6]
nov_seznam = []

for i in range(len(seznam) + 1):
    nov_seznam.append(i)

nov_seznam.pop(3)

print(seznam, nov_seznam)