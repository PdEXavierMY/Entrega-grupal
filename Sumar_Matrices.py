def simpleArraySum(matriz):
    suma = 0
    for i in matriz:
        suma += i
    return suma

def construccion_matriz(matriz):
    filas_columnas = int(input("¿Cuántas filas y columnas tendrá la matriz?(Por favor intrduzca solo un número) "))
    #Se podría modificar reutilizando código para que se repitiese la pregunta si no se introduce un entero
    for j in range(filas_columnas):
        fila_matriz = list(map(int, input().rstrip().split()))
        matriz += [fila_matriz]
    print(matriz)
    return matriz

if __name__ == '__main__':
    matriz = []
    result = simpleArraySum(matriz)
    construccion_matriz(matriz)