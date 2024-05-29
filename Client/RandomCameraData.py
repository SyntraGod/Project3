import random

def randomNumber():
    number = random.randint(0, 20)
    return number

def randomStatus():
    status = random.randint(0,1)
    return status

def randomCamData1():
    data = 'CamData:0001/'
    numIn = randomNumber()
    numOut = randomNumber()
    doorStatus = randomStatus()
    data += str(numIn) + '/' + str(numOut) + '/' + str(doorStatus) + '/1'
    return data

def randomCamData2():
    data = 'CamData:0002/'
    numIn = randomNumber()
    numOut = randomNumber()
    doorStatus = randomStatus()
    data += str(numIn) + '/' + str(numOut) + '/' + str(doorStatus) + '/1'
    return data

