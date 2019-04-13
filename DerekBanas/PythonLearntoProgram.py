"""
#Ask user to enter the name
name = input("Enter your name hoss! : ")

#Print the welcom message
print("Hello", name)
"""

"""
#Ask the user to input 2 values and assign it
num, num2 = input("Enter 2 numbers : ").split()

#Convert them into Integer
num = int(num)
num2 = int(num2)

#Do maths
sum = num+num2

div = num/num2

mul = num*num2

rem = num%num2

#Print
print("{}+{} = {}".format(num, num2, sum))
print("{}/{} = {}".format(num, num2, div))
print("{}*{} = {}".format(num, num2, mul))
print("{}%{} = {}".format(num, num2, rem))
"""

#Receive miles and convert to kilometers

mile = input("Enter your mile to convert : ")
mile = float(mile)
print("%f miles equals to %f kilometers"%(mile, mile*1.60934))