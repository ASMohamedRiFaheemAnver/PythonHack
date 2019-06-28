# https://www.hackerrank.com/challenges/nested-list/tutorial
"""
nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]

# getting the length
print(len(nested_list))

# printing first element set
print(nested_list[0])

# printing first element
print(nested_list[0][0])

"""

# https://stackoverflow.com/questions/30520932/user-input-to-store-in-nested-lists-with-int-conversion-python

"""
x = int(input())
newlist = []

for i in range(x):
    temp_list = input().split(" ")
    newlist.append(temp_list)

print(newlist)

"""

x = int(input())

newList = []

for i in range(x):
    name = input()
    mark = input()

    temp_list = [name, mark]

    newList.append(temp_list)


newList.sort(key = lambda xi: xi[1])

print(newList[1][0])
print(newList[2][0])