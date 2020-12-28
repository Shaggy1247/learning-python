# -----------------------------------------------------------
# Lesson eight
# Learning about List and Tuples
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------

fruits = ["apple", "pear"]
print(fruits)                   # Prints full list
print(fruits[1])                # Prints "pear"
print(fruits[0])                # Prints "apple"

fruits.append("strawberry")     # Adds "strawberry"
print(fruits)                   # Prints full list

fruits[1] = "blueberry"         # Changed "pear" to "blueberry"
print(fruits)                   # Print full list

positions = (2, 3)              # Tuples
color = (255, 255, 255)         # Tuples
print(type(color))              # Prints data type
