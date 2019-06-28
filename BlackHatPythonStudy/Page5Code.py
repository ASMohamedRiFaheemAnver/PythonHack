# !/bin/python3
def sum(numberone, numbertwo):
    numberoneint = convertointeger(numberone)
    numbertwoint = convertointeger(numbertwo)

    return numberoneint + numbertwoint

def convertointeger(numberstring):
    return (int)(numberstring)

print(sum("1", "4"))