# fifth brain game

from random import randint

import prompt


def fifth_task():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def fifth_game(name):
    bottom_bound = 1
    upper_bound = 100
    num = randint(bottom_bound, upper_bound)
    print(f'Question: {num}')
    res = is_prime(num)
    answer = prompt.string('Your answer: ')
    if answer == res:
        return True
    else:
        answer_is_wrong = f"'{answer}' is wrong answer ;(. "
        try_again = f"Correct answer was '{res}'.\nLet's try again, {name}!"
        return print(answer_is_wrong + try_again)


def is_prime(num):
    if num % 2 == 0:
        return 'yes' if num == 2 else 'no'
    index = 3
    while index * index <= num and num % index != 0:
        index += 2
    return 'yes' if index * index > num else 'no'
