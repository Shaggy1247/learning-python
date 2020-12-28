# -----------------------------------------------------------
# Lesson two
# Going over operators and user input by making a calculator
#
# Done 12/27/20, Shaggy1247
# -----------------------------------------------------------
import operator

allowed_operators = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul
}

print('Enter first number.')
number_one = input()            # Getting user input for number_one

print('Enter second number.')
number_two = input()            # Getting user input for number_two

print('Enter math operator.')
math_operator = input()         # Getting user input for math_operator

answer = allowed_operators[math_operator](int(number_one), int(number_two))
print(
    number_one + ' ' + math_operator + ' ' + number_two + ' = ' + str(answer))
