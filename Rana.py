#Lo primero es crear el laberinto de la rana. Lo haremos como en el primer ejemplo, pero podría cambiarse
#Nos basamos en una de nuestras prácticas del laberinto

import random

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
    for valor in rana:
        if valor == (i, j):
            laberinto[i].append("R")
            hayobstaculo = True
            break
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
despliegue_laberinto(laberinto)

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

def movimientos(naleatorio):
    if naleatorio == 1:
        return "Arriba"
    elif naleatorio == 2:
        return "Abajo"
    elif naleatorio == 3:
        return "Derecha"
    elif naleatorio == 4:
        return "Izquierda"

def comparacion(i, j):
    if laberinto[i][j] == "S":
        return (i, j)
    if laberinto[i][j] == "B":
        return (i, j)
    if laberinto[i][j] == "t":
        if (i, j) == tunel1[0]:
            i = tunel1[1][0]
            j = tunel1[1][1]
        else:
            i = tunel1[0][0]
            j = tunel1[0][1]
        return (i, j)
    if laberinto[i][j] == "T":
        if (i, j) == tunel2[0]:
            i = tunel2[1][0]
            j = tunel2[1][1]
        else:
            i = tunel2[0][0]
            j = tunel2[0][1]
        return (i, j)

def juego_rana():
    i = rana[0][0]
    j = rana[0][1]
    while True:
        direccion = random.randint(1, 4)
        movimiento = movimientos(direccion)
        if movimiento == "Arriba" and laberinto[i - 1][j] != "X":
            laberinto[i][j] = " "
            i -= 1
            coordenadas = comparacion(i, j)
            i = coordenadas[0]
            j = coordenadas[1]
        elif movimiento == "Abajo" and laberinto[i + 1][j] != "X":
            laberinto[i][j] = " "
            i += 1
            coordenadas = comparacion(i, j)
            i = coordenadas[0]
            j = coordenadas[1]
        elif movimiento == "Derecha" and laberinto[i][j + 1] != "X":
            laberinto[i][j] = " "
            j += 1
            coordenadas = comparacion(i, j)
            i = coordenadas[0]
            j = coordenadas[1]
        elif movimiento == "Izquierda" and laberinto[i][j - 1] != "X":
            laberinto[i][j] = " "
            j -= 1
            coordenadas = comparacion(i, j)
            i = coordenadas[0]
            j = coordenadas[1]