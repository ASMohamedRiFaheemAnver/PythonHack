import itertools

lst = []
n = int(input())

for i in range(0, n):
    lst.append('k')

lst2 = []
n = int(input())
for i in range(0, n):
    lst2.append('j')

lstfull = []
lstfull = lst + lst2

com = itertools.combinations(lstfull, 3)

# print(list(set(com)))

listFinal = []

listFinal = list(set(com))

listFinalTwo = []

for listOne in listFinal:
    if len(set(listOne)) != 1:
        listFinalTwo.append(listOne)

print(len(listFinalTwo))