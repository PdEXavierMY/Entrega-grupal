#Definir la casa y árboles
#Recta(Eje x) de 0 a 50
#Casa en el intervalo x = (25,30)
#Manzano en x = 20
#Naranjo en x = 35

import random

CASA = (25, 30)
MANZANO = 20
NARANJO = 35
contadormanzanas = 0
contadornaranjas = 0
manzanascaidas = int(input("Introduce el número de manzanas que se han caido del árbol: "))
naranjascaidas = int(input("Introduce el número de naranjas que se han caido del árbol: "))

def contarfrutas(contadormanzanas, contadornaranjas):
    for i in range(manzanascaidas):
        valor_caida_m = random.randint(-15,15)
        manzana = MANZANO - valor_caida_m
        print("La " + str(i +1) + " manzana ha caido en el punto x = " + str(manzana))
        if CASA[0] <= manzana <= CASA[1]:
            contadormanzanas += 1

    for j in range(naranjascaidas):
        valor_caida_n = random.randint(-15,15)
        naranja = MANZANO - valor_caida_n
        print("La " + str(j +1) + " naranja ha caido en el punto x = " + str(naranja))
        if CASA[0] <= naranja <= CASA[1]:
            contadornaranjas += 1

    print("En total han caido " + str(contadormanzanas) + " manzanas en la casa de Sam.")
    print("En total han caido " + str(contadornaranjas) + " naranjas en la casa de Sam.")

if __name__ == '__main__':
    contarfrutas(contadormanzanas, contadornaranjas)