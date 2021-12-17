#Definir la casa y árboles:
#Casa en el intervalo x = (25,30)
#Manzano en x = 20
#Naranjo en x = 35

import random

CASA = tuple(map(int, input("Introduce el intervalo de x en el que está la casa de Sam con dos enteros separados por un espacio(Ej: 25 30): ").rstrip().split()))
MANZANO = int(input("Introduce la posición del manzano: "))
NARANJO = int(input("Introduce la posición del naranjo: "))
contadormanzanas = 0
contadornaranjas = 0
manzanascaidas = int(input("Introduce el número de manzanas que se han caido del árbol: "))
naranjascaidas = int(input("Introduce el número de naranjas que se han caido del árbol: "))
rangocaida = int(input("Introduzca la distancia máxima(en valor absoluto) que puede recorrer la fruta desde que se cae del árbol hasta que para: "))
#Variables iniciales definidas por el usuario

def contarfrutas(contadormanzanas, contadornaranjas):
    for i in range(manzanascaidas):
        valor_caida_m = random.randint(-rangocaida,rangocaida) #Cuanto se desplaza la fruta
        #Se puede ampliar aunque reduce la posibilidad de caer en la casa
        manzana = MANZANO - valor_caida_m #Donde se queda la fruta
        print("La " + str(i +1) + " manzana ha caido en el punto x = " + str(manzana))
        if CASA[0] <= manzana <= CASA[1]:
            contadormanzanas += 1

    for j in range(naranjascaidas):
        valor_caida_n = random.randint(-rangocaida,rangocaida) #Cuanto se desplaza la fruta
        #Se puede ampliar aunque reduce la posibilidad de caer en la casa
        naranja = MANZANO - valor_caida_n #Donde se queda la fruta
        print("La " + str(j +1) + " naranja ha caido en el punto x = " + str(naranja))
        if CASA[0] <= naranja <= CASA[1]:
            contadornaranjas += 1

    print("En total han caido " + str(contadormanzanas) + " manzanas en la casa de Sam.")
    print("En total han caido " + str(contadornaranjas) + " naranjas en la casa de Sam.")

if __name__ == '__main__':
    print("La casa de Sam está en el intervalo x = " + str(CASA))
    contarfrutas(contadormanzanas, contadornaranjas)