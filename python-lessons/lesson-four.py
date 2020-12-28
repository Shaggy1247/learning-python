# -----------------------------------------------------------
# Lesson four
# Learning about If else staments
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------
age = input('Input your age: ')

if int(age) == 16:
    print("Hey you're 16")

if int(age) > 16:
    print("Hey you're older than 16")
else:
    print("You're younger than 16")

height = input("What is you're height: ")

if int(height) <= 1:
    print("You cannot ride, under 1m")
elif int(height) >= 5:
    print("Wow you are tall!")
elif int(height) > 2:
    print("You cannot ride, over 2m")
else:
    print("You can ride!")
