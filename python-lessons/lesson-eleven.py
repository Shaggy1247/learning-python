# -----------------------------------------------------------
# Lesson eleven
# Learning about slice operator
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------

fruits = ["apples", "pear", "strawberry"]
text = "Hello I like Python"

# print(text[start:stop:step])

print(text[0:5])
print(text[:8])
print(text[1:])
print(text[::2])
print(text[::4])
print(fruits[1:])
print(fruits[::2])
fruits[0:0] = "blueberry"
print(fruits)
