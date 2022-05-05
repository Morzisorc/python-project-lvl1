# fifth brain game

from random import randint

import prompt


def fifth_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def fifth_game(name):
    num = randint(1, 100)
    print(f'Question: {num}')
    res = is_prime(num)
    answer = prompt.string('Your answer: ')
    if answer == res:
        return True
    else:
        return print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.\nLet's try again, {name}!")


def is_prime(num):
    if num % 2 == 0:
        return 'yes' if num == 2 else 'no'
    index = 3
    while index * index <= num and num % index != 0:
        index += 2
    return 'yes' if index * index > num else 'no'
