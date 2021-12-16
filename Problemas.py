import random

a = []
for i in range(3):
    a.append(random.randint(0,100))

b = []
for i in range(3):
    b.append(random.randint(0,100))

def compareTriplets():
    score1 = 0
    score2 = 0

    for i in range(3):
        if a[i] > b[i]:
            score1 = score1 + 1

        elif a[i] < b[i]:
            score2 = score2 + 1

    lista = [score1, score2]
    print("Las puntuaciones son: " + str(lista))
    




if __name__ == "__Main__":
    compareTriplets()



