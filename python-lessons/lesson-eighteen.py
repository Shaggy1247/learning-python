# -----------------------------------------------------------
# Lesson eighteen
# Learning about error handling
#
# Done 12/31/20, Shaggy1247
# -----------------------------------------------------------

text = input("Username: ")
try:
    number = int(text)
    print(number)
except:     # Not best practice
    print("invalid Username: ")
