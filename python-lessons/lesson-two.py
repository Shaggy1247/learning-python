import operator

allowed_operators = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul
}

print('Enter first number.')
number_one = input()

print('Enter second number.')
number_two = input()

print('Enter math operator.')
math_operator = input()

answer = allowed_operators[math_operator](int(number_one), int(number_two))
print(
    number_one + ' ' + math_operator + ' ' + number_two + ' = ' + str(answer))
