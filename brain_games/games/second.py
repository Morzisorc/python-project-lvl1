# second brain game

from random import randint

import prompt


def second_task():
    print('What is the result of the expression?')


def second_game(name):
    bottom_bound = 1
    upper_bound = 30
    num1 = randint(bottom_bound, upper_bound)
    num2 = randint(bottom_bound, upper_bound)
    sign_num = randint(1, 3)
    if sign_num == 1:  # знак +
        print(f'Question: {str(num1)} + {str(num2)}')
        res = num1 + num2
    elif sign_num == 2:  # знак -
        print(f'Question: {str(num1)} - {str(num2)}')
        res = num1 - num2
    elif sign_num == 3:  # знак *
        print(f'Question: {str(num1)} * {str(num2)}')
        res = num1 * num2

    answer = prompt.string('Your answer: ')
    if int(answer) == res:
        return True
    else:
        return print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.\nLet's try again, {name}!")
