# -----------------------------------------------------------
# Lesson seventeen
# Learning about optional parameters
#
# Done 12/31/20, Shaggy1247
# -----------------------------------------------------------

def func(x=3, text="2"):          # has a default value
    print(x)
    if text == "1":
        print("text is 1")
    else:
        print("text is not 1")


func()
