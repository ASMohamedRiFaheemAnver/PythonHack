from itertools import permutations

string, number = input().split()

for c in permutations(sorted(string), int(number)):
    print(''.join(c))