# -----------------------------------------------------------
# Lesson thirteen
# Learning about reading text file
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------


file = open('python-lessons/readfile.txt', 'r')
f = file.readlines()

print(f)

newList = []
for line in f:                          # check by line
    if line[-1] == "\n":
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)

for line in f:                          # easier way to clean up
    newList.append(line.strip())

print(newList)
