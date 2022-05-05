# third brain game

from random import randint

import prompt


def third_task():
    print('Find the greatest common divisor of given numbers.')


def third_game(name):
    bottom_bound = 1
    upper_bound = 100
    max_num = randint(bottom_bound, upper_bound)
    min_num = randint(bottom_bound, upper_bound)
    print(f'Question: {max_num} {min_num}')
    if min_num > max_num:
        (max_num, min_num) = (min_num, max_num)  # делаем максимальное максимальным
    res = find_gcd(max_num, min_num)
    answer = prompt.integer('Your answer: ')
    if answer == res:
        return True
    else:
        return print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.\nLet's try again, {name}!")


def find_gcd(max_num, min_num):
    remainder = max_num % min_num
    if remainder != 0:
        return find_gcd(min_num, remainder)
    else:
        return min_num
