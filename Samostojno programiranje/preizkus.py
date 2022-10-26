rezultati = [108.9, 107.0, 109.3, 109.8, 108.7,
            110.8, 110.2, 111.5, 113.5, 110.1]

def razlika_casov(r):
    najkraj = min(r)
    najdalj= max(r)
    print(najkraj)
    print(najdalj)
    return najdalj-najkraj

print(razlika_casov(rezultati))