#Lo primero es crear el laberinto de la rana. Lo haremos como en el primer ejemplo, pero podría cambiarse
#Nos basamos en una de nuestras prácticas del laberinto

import random
import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos', 'ce'):
        command = 'cls'
    os.system(command)

muro = ((0,5), (1,3), (1,4), (2,2), (2,3), (2,7), (3,3), (4,3))
bombas = ((3,2),(3,6), (3,7))
tunel1 = ((0,2), (4,0))
tunel2 = ((0,4), (2,4))
salidas = ((0,7), (4,7))
rana = ((1,0))

estructura = len(muro)
filas = 5
columnas = 8
#Se define con antelación el número de filas y columnas del laberinto, los muros, bombas y demás
laberinto = [[]]
for l in range(filas - 1):
    laberinto += [[]]

def obstaculos(i, j):
    hayobstaculo = False
    for valor in muro:
        if valor == (i, j):
            laberinto[i].append("X")
            hayobstaculo = True
            break
    for valor in bombas:
        if valor == (i, j):
            laberinto[i].append("B")
            hayobstaculo = True
            break
    for valor in tunel1:
        if valor == (i, j):
            laberinto[i].append("t")
            hayobstaculo = True
            break
    for valor in tunel2:
        if valor == (i, j):
            laberinto[i].append("T")
            hayobstaculo = True
            break
    for valor in salidas:
        if valor == (i, j):
            laberinto[i].append("S")
            hayobstaculo = True
            break
    if rana == (i, j):
        laberinto[i].append("R")
        hayobstaculo = True
    if hayobstaculo == False:
        laberinto[i].append(" ")
    return laberinto

for i in range(filas):
    for j in range(columnas):
        obstaculos(i, j)

def despliegue_laberinto(laberinto):
    for z in range(len(laberinto) - 1):
        print(str(laberinto[z]) +  ",")
    print(laberinto[len(laberinto) - 1])

for i in range(filas):
    laberinto[i] += ["X"]
for i in range(filas):
    laberinto[i] = ["X"] + laberinto[i]
techo_y_suelo = [["X"]]
for i in range(columnas + 1):
    techo_y_suelo[0] += ["X"]
laberinto = techo_y_suelo + laberinto
laberinto += techo_y_suelo
#Se añaden dos filas/columnas al laberinto por cada lado para evitar errores al comparar con las casillas de alrededor
tunel1 = ((tunel1[0][0] + 1,tunel1[0][1] + 1), (tunel1[1][0] + 1,tunel1[1][1] + 1))
tunel2 = ((tunel2[0][0] + 1,tunel2[0][1] + 1), (tunel2[1][0] + 1,tunel2[1][1] + 1))
#Se cambian las coordenadas del tunel ya que el laberinto se ha ampliado con una capa de muros externa

def comparacion(i, j):
    if laberinto[i][j] == "S":
        print("La rana ha salido del laberinto, fin de la partida :)")
        return (i, j, True)
    elif laberinto[i][j] == "B":
        print("La rana ha caido en una bomba, fin de la partida :(")
        return (i, j, True)
    elif laberinto[i][j] == "t":
        if (i, j) == tunel1[0]:
            i = tunel1[1][0]
            j = tunel1[1][1]
        else:
            i = tunel1[0][0]
            j = tunel1[0][1]
        clearConsole()
        return (i, j, False)
    elif laberinto[i][j] == "T":
        if (i, j) == tunel2[0]:
            i = tunel2[1][0]
            j = tunel2[1][1]
        else:
            i = tunel2[0][0]
            j = tunel2[0][1]
        clearConsole()
        return (i, j, False)
    else:
        clearConsole()
        return (i, j, False)

def juego_rana():
    posible_direccion = ["Arriba", "Abajo", "Derecha", "Izquierda"]
    i = rana[0] + 1
    j = rana[1]+ 1
    while True:
        direccion = random.choice(posible_direccion)
        if direccion == "Arriba" and laberinto[i - 1][j] != "X":
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = " "
            i -= 1
            coordenadas = tuple(comparacion(i, j))
            i = coordenadas[0]
            j = coordenadas[1]
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = "R"
            despliegue_laberinto(laberinto)
            time.sleep(0.25)
            if coordenadas[2] == True:
                break
        elif direccion == "Abajo" and laberinto[i + 1][j] != "X":
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = " "
            i += 1
            coordenadas = tuple(comparacion(i, j))
            i = coordenadas[0]
            j = coordenadas[1]
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = "R"
            despliegue_laberinto(laberinto)
            time.sleep(0.25)
            if coordenadas[2] == True:
                break
        elif direccion == "Derecha" and laberinto[i][j + 1] != "X":
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = " "
            j += 1
            coordenadas = tuple(comparacion(i, j))
            i = coordenadas[0]
            j = coordenadas[1]
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = "R"
            despliegue_laberinto(laberinto)
            time.sleep(0.25)
            if coordenadas[2] == True:
                break
        elif direccion == "Izquierda" and laberinto[i][j - 1] != "X":
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = " "
            j -= 1
            coordenadas = tuple(comparacion(i, j))
            i = coordenadas[0]
            j = coordenadas[1]
            if laberinto[i][j] != "T" and laberinto[i][j] != "t":
                laberinto[i][j] = "R"
            despliegue_laberinto(laberinto)
            time.sleep(0.25)
            if coordenadas[2] == True:
                break

if __name__ == '__main__':
    juego_rana()