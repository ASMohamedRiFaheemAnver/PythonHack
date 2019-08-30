import collections

numberofShoes = int(input())

shoes = collections.Counter(map(int, input().split()))
numberofCustomer = int(input())

income = 0
for i in range(numberofCustomer):
    size, prize = map(int, input().split())
    if shoes[size]:
        income += prize
        shoes[size] -= 1


print(income)