from itertools import product

arrone = map(int, input().split())
arrtwo = map(int, input().split())

# https://stackoverflow.com/questions/37625208/printing-an-int-list-in-a-single-line-python3
print(' '.join(str(i) for i in list(product(arrone, arrtwo))))