def simpleArraySum(matriz):
    suma = 0
    for lista in matriz:
    #Se cogen los elementos dentro de matriz(en este caso cada lista dentro de las listas) uno por uno
        for elemento in lista:
            suma += elemento
            #Se recorre cada elemento dentro de la lista y se suman
    return suma

def construccion_matriz():
    matriz = []
    filas = int(input("¿Cuántas filas tendrá la matriz?(Por favor intrduzca solo un número) "))
    print("Todas las filas deben tener el mismo número de elementos.")
    print("Si alguna fila tiene más elementos que la anterior, se eliminarán los últimos elementos de esta hasta que en cada fila haya el mismo número de elementos.")
    print("Si alguna fila tiene menos elementos que la anterior, se añádirán 0 hasta que en cada fila haya el mismo número de elementos.")
    for i in range(filas):
        print("Introduzca los números de la fila separados solamente por un espacio:")
        fila_matriz = list(map(int, input().rstrip().split()))
        #Creas una fila(como está dentro de un bucle creas tantas como veces se repite el bucle)
        #(Se podría modificar para que se repitiese la pregunta si no se introducen solo enteros)
        matriz += [fila_matriz]
        #Añades cada fila(que es una lista) a una lista
    columnas = len(matriz[0])
    for j in matriz:
        while len(j) > columnas:
            j.pop()
        while len(j) < columnas:
            j.append(0)
        #Si metes filas más grandes que la primera te quita elementos, y si te faltan elementos en una fila te añade 0
    print("La matriz construida es la siguiente: " + str(matriz))
    return matriz

if __name__ == '__main__':
    matriz = construccion_matriz()
    result = simpleArraySum(matriz)
    print("La suma total de todos los elementos de la matriz es " + str(result))