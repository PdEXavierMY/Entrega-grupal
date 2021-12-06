def simpleArraySum(matriz):
    suma = 0
    for i in matriz:
        suma += i
    return suma

if __name__ == '__main__':
    matriz = list(map(int, input().rstrip().split()))
    print(matriz)
    result = simpleArraySum(matriz)