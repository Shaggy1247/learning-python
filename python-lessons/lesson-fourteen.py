# -----------------------------------------------------------
# Lesson fourteen
# Learning about writing to a text file
#
# Done 12/31/20, Shaggy1247
# -----------------------------------------------------------

file = open("python-lessons/writefile.txt", "w")

file.write("python\n")
file.write("I am learning to write to a file")

file.close()
