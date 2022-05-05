# first brain game

from random import randint

import prompt


def first_task():  # был вариант все тексты заданий вынести в отдельный файл
    print('Answer "yes" if the number is even, otherwise answer "no".')


def first_game(name):
    num = randint(1, 100)
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    return True if answer == is_even(num) else print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(num)}'.\nLet's try again, {name}!")


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'
