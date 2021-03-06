# forth brain game

from random import randint

import prompt


def forth_task():
    print('What number is missing in the progression?')


def forth_game(name):
    step = randint(1, 10)
    start_num = randint(1, 20)
    blank_position = randint(0, 9)
    index = 0
    sequence = ""
    while index < 10:
        if index == blank_position:
            sequence += " .."
        else:
            sequence += f' {start_num + index * step}'
        index += 1
    print(f'Question:{sequence}')
    res = start_num + step * blank_position
    answer = prompt.integer('Your answer: ')
    if answer == res:
        return True
    else:
        answer_is_wrong = f"'{answer}' is wrong answer ;(. "
        try_again = f"Correct answer was '{res}'.\nLet's try again, {name}!"
        return print(answer_is_wrong + try_again)
