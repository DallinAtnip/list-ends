'''
a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of
only the first and last elements of the given list.
Dallin Atnip 06/01/19
'''

number1 = input("give me a number: ")
number2 = input("give me a number: ")
number3 = input("give me a number: ")
number4 = input("give me a number: ")
number5 = input("give me a number: ")
x = []
x.append(number1)
x.append(number2)
x.append(number3)
x.append(number4)
x.append(number5)


print ("the list is: " + str(x))
userlist = [x[0],x[-1]]
print (userlist)


#    print (x[0],x[-1]) 