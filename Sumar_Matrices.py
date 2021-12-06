def simpleArraySum(matriz):
    suma = 0
    for i in matriz:
        suma += i
    return suma

def construccion_matriz():
    matriz = []
    filas = int(input("¿Cuántas filas tendrá la matriz?(Por favor intrduzca solo un número) "))
    #Se podría modificar reutilizando código para que se repitiese la pregunta si no se introduce un entero
    print("Todas las filas deben tener el mismo número de elementos.")
    print("Si alguna fila tiene más elementos que la anterior, se eliminarán los últimos elementos de esta hasta que en cada fila haya el mismo número de elementos.")
    print("Si alguna fila tiene menos elementos que la anterior, se añádirán 0 hasta que en cada fila haya el mismo número de elementos.")
    for i in range(filas):
        print("Introduzca los números de la fila separados solamente por un espacio")
        fila_matriz = list(map(int, input().rstrip().split()))
        #Se podría modificar reutilizando código para que se repitiese la pregunta si no se introducen solo enteros
        matriz += [fila_matriz]
    columnas = len(matriz[0])
    for j in matriz:
        while len(j) > columnas:
            j.pop()
        while len(j) < columnas:
            j.append(0)
    print(matriz)
    return matriz

if __name__ == '__main__':
    matriz = construccion_matriz()
    result = simpleArraySum(matriz)
    print("La suma total de todos los elementos de una matriz es " + str(result))