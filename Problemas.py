import random

a = []
for i in range(3):
    a.append(random.randint(0,100))
print("La calificación del desafío de Lucía es: " + str(a))

b = []
for i in range(3):
    b.append(random.randint(0,100))
print("La calificación del desafío de Carlos es: " + str(b))

def compareTriplets():
    score1 = 0
    score2 = 0

    for i in range(3):
        if a[i] > b[i]:
            score1 = score1 + 1

        elif a[i] < b[i]:
            score2 = score2 + 1

    lista = ["Lucía: " + str(score1), "Carlos: " + str(score2)]
    print("Las puntuaciones son: " + str(lista))
    




if __name__ == "__main__":
    compareTriplets()



