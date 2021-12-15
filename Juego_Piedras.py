#Juego de piedras

import random

def casospiedras(npiedras):
    if npiedras == 2:
        npiedras -= 2
        print("2 piedras")
    elif npiedras == 3:
        npiedras -= 3
        print("3 piedras")
    elif npiedras == 4:
        npiedras -= 3
        print("3 piedras")
    elif npiedras == 5:
        npiedras -= 5
        print("5 piedras")
    elif npiedras == 6:
        npiedras -= 5
        print("5 piedras")
    elif npiedras == 9:
        npiedras -= 2
        print("2 piedras")
    elif npiedras == 10:
        n = random.choice(2, 3)
        npiedras -= n
        print(str(n) + " piedras")
    elif npiedras == 11:
        npiedras -= 3
        print("3 piedras")
    elif npiedras == 12:
        npiedras -= 5
        print("5 piedras")
    elif npiedras == 13:
        npiedras -= 5
        print("5 piedras")

def juegopiedras(npiedras):
    #movimientosposibles = [2, 3, 5]
    turno = 1
    while True:
        if turno == 1: #Jugador 1
            if npiedras < 2:
                print("Jugador 1 ha perdido, no puede extraer piedras")
                break
            else:
                if npiedras < 20:
                    casospiedras(npiedras)
                    print("Jugador 1 quita ", end="")
                    print("Quedan " + str(npiedras) + " piedras.")
                else:
                    movimiento = random.choice(2, 3, 5)
                    npiedras -= movimiento
                    print("Jugador 1 quita " + str(movimiento) + " piedras.")
                    turno = 2