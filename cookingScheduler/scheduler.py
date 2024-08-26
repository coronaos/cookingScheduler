from main import Excel
from random import randint
import numpy as np

def scheduler():
    datos = Excel()
    days = [1, 2, 3, 4, 5, 6, 7]
    lunch = []
    dinner = []
    nPlates = len(datos.data)-1
    specialPlates = []
    normalPlates = []
    finalSchedule = np.array([
    ["data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111"],
    ["data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111", "data1111111111111111111111111"]])

    for x in range(nPlates):
        if(datos.data.values[x][1] == 5):
            specialPlates.append(datos.data.values[x])
        else:
            normalPlates.append(datos.data.values[x])


    for i in days:
        if(i == 5):
            random = randint(0, len(specialPlates)-1)
            dinner.append(specialPlates[random])
            specialPlates.pop(random)
        elif(i != 5 and i != 7):
            random = randint(0, len(normalPlates) - 1)
            dinner.append(normalPlates[random])
            normalPlates.pop(random)

        random = randint(0, len(normalPlates) - 1)
        lunch.append(normalPlates[random])
        normalPlates.pop(random)
    dinner.append(np.array(['AYUNO']))
    for a in days:
        send = lunch[a-1][0]
        send2 = dinner[a-1][0]

        finalSchedule[0][a-1] = send
        finalSchedule[1][a-1] = send2


    return finalSchedule

