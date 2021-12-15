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
    elif npiedras == 7:
        n = random.choice(movimientosposibles)
        npiedras -= n
        print(str(n) + " piedras")
    elif npiedras == 8:
        n = random.choice(movimientosposibles)
        npiedras -= n
        print(str(n) + " piedras")
    elif npiedras == 9:
        npiedras -= 2
        print("2 piedras")
    elif npiedras == 10:
        n = random.randint(2, 3)
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
    elif npiedras == 14:
        n = random.choice(movimientosposibles)
        npiedras -= n
        print(str(n) + " piedras")
    elif npiedras == 15:
        n = random.choice(movimientosposibles)
        npiedras -= n
        print(str(n) + " piedras")
    elif npiedras == 16:
        npiedras -= 2
        print("2 piedras")
    elif npiedras == 17:
        n = random.randint(2, 3)
        npiedras -= n
        print(str(n) + " piedras")
    elif npiedras == 18:
        npiedras -= 3
        print("3 piedras")
    elif npiedras == 19:
        npiedras -= 5
        print("5 piedras")
    elif npiedras == 20:
        npiedras -= 5
        print("5 piedras")
    return npiedras
    

movimientosposibles = [2, 3, 5]
npiedras = int(input("¿Con cuántas piedras se va a jugar?: "))
turno = 1
while True:
    if turno == 1: #Jugador 1
        if npiedras < 2:
            print("Jugador 1 ha perdido, no puede extraer piedras.")
            break
        else:
            if npiedras <= 20:
                print("Jugador 1 quita ", end="")
                npiedras = casospiedras(npiedras)
                print("Quedan " + str(npiedras) + " piedras.")
                turno = 2
            else:
                movimiento = random.choice(movimientosposibles)
                npiedras -= movimiento
                print("Jugador 1 quita " + str(movimiento) + " piedras.")
                turno = 2
    if turno == 2: #Jugador 2
        if npiedras < 2:
            print("Jugador 2 ha perdido, no puede extraer piedras.")
            break
        else:
            if npiedras < 20:
                print("Jugador 2 quita ", end="")
                npiedras = casospiedras(npiedras)
                print("Quedan " + str(npiedras) + " piedras.")
                turno = 1
            else:
                movimiento = random.choice(movimientosposibles)
                npiedras -= movimiento
                print("Jugador 2 quita " + str(movimiento) + " piedras.")
                turno = 1