import itertools

totalSum, startingPoint, endingPoint = input().split()

listOfNumbers = []
sumOfNumbersMax = 0
sumOfNumbersMin = 0
maxIter = 0
minIter = 0
while totalSum > sumOfNumbersMax:
    sumOfNumbersMax += startingPoint
    maxIter = maxIter + 1

while totalSum > sumOfNumbersMin:
    sumOfNumbersMin += endingPoint
    minIter = minIter + 1

maxIter = maxIter

for i in range(startingPoint, endingPoint+1):
    for j in range(maxIter):
        listOfNumbers.append(i)

comOne = itertools.combinations(listOfNumbers, minIter)
comTwo = itertools.combinations(listOfNumbers, maxIter)

comFinal = list(comOne) + list(comTwo)

result = []
isExist = False

for comElem in comFinal:
    sumT = 0
    for oneNumber in comElem:
        sumT += oneNumber
    if sumT == totalSum:
        result = comElem
        isExist = True
        break

if isExist:
    print("YES")
    for numb in result:
        print(numb, end=" ")
else:
    print("NO")
