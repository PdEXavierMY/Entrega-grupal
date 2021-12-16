#Lo primero es crear el laberinto de la rana. Lo haremos como en el primer ejemplo, pero podría cambiarse
#Nos basamos en una de nuestras prácticas del laberinto

muro = ((0,5), (1,3), (1,4), (2,2), (2,3), (2,7), (3,3), (4,3))
bombas = ((3,2),(3,6), (3,7))
tunel1 = ((0,2), (4,0))
tunel2 = ((0,4), (2,4))
salidas = ((0,7), (4,7))

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
    if hayobstaculo == False:
        laberinto[i].append(" ")
    return laberinto

for i in range(filas):
    for j in range(columnas):
        obstaculos(i, j)

def despliegue_laberinto():
    for z in range(len(laberinto) - 1):
        print(str(laberinto[z]) +  ",")
    print(laberinto[len(laberinto) - 1])
despliegue_laberinto()