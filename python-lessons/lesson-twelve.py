# -----------------------------------------------------------
# Lesson twleve
# Learning about functions
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------

def addTwo(x):
    return x + 2


def subtractTwo(number):
    return number - 2


def printString(string):
    print(string)


def accel(mass, force):
    a = mass * force
    return a


def doSomthing():
    print("Hello")


newNumber = subtractTwo(3)
print(newNumber)
print(addTwo(5))
printString("Hello ")
printString("My name is Traven")
doSomthing()
print(accel(2, 5))
