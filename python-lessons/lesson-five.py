# -----------------------------------------------------------
# Lesson five
# Learning about Chanined Conditionals & Nested Statements
#
# Done 12/28/20, Shaggy1247
# -----------------------------------------------------------
x = 2
y = 3

if x == y and x + y == 5:           # Both are not true and will not run
    print("and")
elif y == x or x + y == 5:          # One is true and will run
    print("or")
elif not(y == x or x + y == 6):     # Both are false Will not run
    print("if not")
else:
    print(":(")

if x == 2:
    if y == 3:
        print("x == 2, y == 3")
    else:
        print("x == 2, y != 3")
else:
    print('x != 2')
