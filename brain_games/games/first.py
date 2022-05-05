# first brain game

from random import randint

import prompt


def first_task():  # был вариант все тексты заданий вынести в отдельный файл
    print('Answer "yes" if the number is even, otherwise answer "no".')


def first_game(name):
    bottom_bound = 1
    upper_bound = 100
    num = randint(bottom_bound, upper_bound)
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    if answer == is_even(num):
        return True
    else:
        return print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(num)}'.\nLet's try again, {name}!")


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'
