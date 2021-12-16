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

def contarfrutas():
    for i in range(manzanascaidas):
        valor_caida_m = random.randint(-15,15)
        manzana = MANZANO - valor_caida_m
        if CASA[0] <= manzana <= CASA[1]:
            contadormanzanas += 1

    for j in range(naranjascaidas):
        valor_caida_n = random.randint(-15,15)
        naranja = MANZANO - valor_caida_m
        if CASA[0] <= naranja <= CASA[1]:
            contadornaranjas += 1