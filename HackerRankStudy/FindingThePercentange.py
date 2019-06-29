# https://www.hackerrank.com/challenges/finding-the-percentage/problem

# https://www.w3schools.com/python/ref_func_map.asp

"""
# defining a function
def myfunc(n):
    return len(n)


# let map apply the myfunc to every element and return the list address
x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
print(list(x))
"""

"""
def myfunc(a, b, c):
    return a + b + c


x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'), ('apple', 'banana', 'cherry'))

print(x)
print(list(x))
"""

"""
# getting first element as name and other following as line split by " " 
name, *line = input().split()

print(name)

# printing line elements from element 2
print(line[1:])
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    newList = student_marks[query_name]
    # print("%.2f"%(sum(newList)/len(newList)))
    print("{0:.2f}".format(sum(newList)/len(newList)))