# -----------------------------------------------------------
# Lesson nineteen
# Learning about Global vs Local variables
#
# Done 12/31/20, Shaggy1247
# -----------------------------------------------------------

var = 9            # Global
loop = True        # Global


def func(x):
    newVar = 7      # newvVar is local to func()
    if x == 5:
        return newVar


def otherFunc(number):
    global var      # looks for variable out of function
    var = 10
    if number == 5:
        var - 5
        return var
    else:
        print("Not 5")


print(func(5))
