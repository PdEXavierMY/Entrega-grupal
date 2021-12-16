#Lo primero es crear el laberinto de la rana. Lo haremos como en el primer ejemplo, pero podría cambiarse
#Nos basamos en una de nuestras prácticas del laberinto

muro = ((0,5), (1,3), (1,4), (2,2), (2,3), (2,7), (3,3), (4,3))
bombas = ((3,2),(3,6), (3,7))
tunel1 = ((0,2), (7,0))
tunel2 = ((0,4), (2,4))
salidas = ((0,7), (7,7))

estructura = len(muro)
filas = 5
columnas = 8
#Se define con antelación el número de filas y columnas del laberinto, los muros, bombas y demás
laberinto = [[]]
for l in range(filas - 1):
    laberinto += [[]]

def comparacion(i, j):
    haymuro = False
    for valor in range(estructura):
        if muro[valor] == (i, j):
            laberinto[i].append("X")
            haymuro = True
            break
    if haymuro == False:
        laberinto[i].append(" ")
    return laberinto

for i in range(filas):
    for j in range(columnas):
        comparacion(i, j)

def despliegue_laberinto():
    for z in range(len(laberinto) - 1):
        print(str(laberinto[z]) +  ",")
    print(laberinto[len(laberinto) - 1])
despliegue_laberinto()