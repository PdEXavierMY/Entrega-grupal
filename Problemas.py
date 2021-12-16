import random

a = []
for i in range(3):
    a.append(random.randint(0,100))

b = []
for i in range(3):
    b.append(random.randint(0,100))

def primer_elemento():
    score1 = 0
    score2 = 0

    if a[0] > b[0]:
        score1 = score1 + 1
        score2 = score2

    elif a[0] < b[0]:
        score1 = score1
        score2 = score2 + 1

    else:
        score1 = score1
        score2 = score2

    return score1, score2

def segundo_elemento():
    score1 = 0
    score2 = 0

    if a[1] > b[1]:
        score1 = score1 + 1
        score2 = score2

    elif a[1] < b[1]:
        score1 = score1
        score2 = score2 + 1

    else:
        score1 = score1
        score2 = score2

    return score1, score2

def tercer_elemento():
    score1 = 0
    score2 = 0

    if a[2] > b[2]:
        score1 = score1 + 1
        score2 = score2

    elif a[2] < b[2]:
        score1 = score1
        score2 = score2 + 1

    else:
        score1 = score1
        score2 = score2
    
    return score1, score2
    





def compareTriplets():
    d = primer_elemento()
    f = segundo_elemento()
    g = tercer_elemento()
    
    puntuacion = [score1, score2]
    print(puntuacion)
    
if __name__ == "__Main__":
    compareTriplets()



