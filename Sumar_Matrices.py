def simpleArraySum(matriz):
    suma = 0
    for i in matriz:
        suma += i
    return suma

def construccion_matriz(matriz):
    filas = int(input("¿Cuántas filas y columnas tendrá la matriz?(Por favor intrduzca solo un número) "))
    #Se podría modificar reutilizando código para que se repitiese la pregunta si no se introduce un entero
    for i in range(filas):
        print("Introduzca los números de la fila separados solamente por un espacio")
        fila_matriz = list(map(int, input().rstrip().split()))
        matriz += [fila_matriz]
    columnas = len(matriz[0])
    for j in matriz:
        while len(matriz[j]) > columnas:
            matriz.pop(j)
    print(matriz)
    return matriz

if __name__ == '__main__':
    matriz = []
    result = simpleArraySum(matriz)
    construccion_matriz(matriz)