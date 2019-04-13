#https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    
    if(year%400<1):
        leap = True
    elif(year%100<1):
        leap = False
    elif(year%4<1):
        leap = True
    
    
    return leap

year = int(input())
print(is_leap(year))