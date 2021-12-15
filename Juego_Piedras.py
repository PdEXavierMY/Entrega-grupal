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
    