# first brain game
from random import randint
import prompt
from common import welcome, say_hello, start_game


def main():
    welcome() #приветствует игрока
    name = say_hello() #узнет и запоминает имя, здоровается
    print('What is the result of the expression?')
    start_game(2, name)


def second_game(name):
    num1 = randint(1, 30)
    num2 = randint(1, 30)
    sign_num = randint(1,3)
    if sign_num == 1: #знак +
        print(f'Question: {str(num1)} + {str(num2)}')
        result = num1 + num2
    elif sign_num == 2: #знак -
        print(f'Question: {str(num1)} - {str(num2)}')
        result = num1 - num2
    elif sign_num == 3: #знак *
        print(f'Question: {str(num1)} * {str(num2)}')
        result = num1 * num2
    
    answer = prompt.string('Your answer: ')
    return True if answer == result else print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
     