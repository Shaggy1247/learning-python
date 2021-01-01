# -----------------------------------------------------------
# Lesson fifteen
# Learning about .count() and .find()
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------

# .find(), .count()
string = "hello"
print(string.find("l"))     # Gives where the first one is found
print(string.find("h"))
print(string.find("t"))     # Does not find "t" returning -1
print(string.count("l"))    # Gives how many exist
print(string.count("h"))


while string:
    string = input("Type something: ")
    if string.count("_") > 0:
        print("Not good!")
    else:
        print("good")
        break
