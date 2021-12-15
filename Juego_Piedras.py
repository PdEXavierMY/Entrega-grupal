#Juego de piedras

import random

def casospiedrasfavorables(npiedras):
    if npiedras == 2:
        npiedras -= 2
    elif npiedras == 3:
        npiedras -= 3
    elif npiedras == 4:
        npiedras -= 3
    elif npiedras == 5:
        npiedras -= 5
    elif npiedras == 6:
        npiedras -= 5
    elif npiedras == 9:
        npiedras -= 2
    elif npiedras == 10:
        npiedras -= random.choice(2, 3)
    elif npiedras == 11:
        npiedras -= 3
    elif npiedras == 12:
        npiedras -= 5
    elif npiedras == 13:
        npiedras -= 5

def juegopiedras(npiedras):
    #movimientosposibles = [2, 3, 5]
    turno = 1
    while turno == 1: #Jugador 1
        finmovimiento = False
        if npiedras < 2:
            print("Jugador 1 ha perdido, no puede extraer piedras")
            break
        else:
            if npiedras < 13:
                casospiedrasfavorables(npiedras)
                print("Jugador 1 quita ", end="")
                print("Quedan " + str(npiedras) + " piedras.")
            else:
                if finmovimiento == True:
                    turno = 2
    while turno == 2: #Jugador 2
    