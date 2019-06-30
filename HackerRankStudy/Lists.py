# https://www.hackerrank.com/challenges/python-lists/problem

newList = []

n = int(input())

for _ in range(n):
    userInput = input().split(" ")

    if userInput[0] == "insert":
        newList.insert(int(userInput[1]), int(userInput[2]))
    elif userInput[0] == "print":
        print(newList)
    elif userInput[0] == "remove":
        newList.remove(int(userInput[1]))
    elif userInput[0] == "append":
        newList.append(int(userInput[1]))
    elif userInput[0] == "sort":
        newList.sort()
    elif userInput[0] == "pop":
        newList.pop()
    elif userInput[0] == "reverse":
        newList.reverse()