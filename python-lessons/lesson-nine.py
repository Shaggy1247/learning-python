# -----------------------------------------------------------
# Lesson nine
# Learning about iteration by item
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------

fruits = "apple", "pear", "blueberry"

for fruit in fruits:    # prints out whole list
    print(fruit)

for fruit in fruits:    # Prints out item in list
    if fruit == "blueberry":
        print("blueberry")
    else:
        print("not a blueberry")
