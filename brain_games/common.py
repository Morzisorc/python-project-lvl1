import prompt
from brain_games.games.first import first_game
from brain_games.games.second import second_game


def welcome():
     print('Welcome to the Brain Games!')

def say_hello():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def start_game(game_num, name):
    count = 0
    while count < 3:
        #запуск раунда и проверка, выигран ли он
        if is_round_won(game_num, name):
            count += 1
            print('Correct!')

        #проверка на 3 победы
        if count == 3:
            return print(f'Congratulations, {name}!')


def is_round_won(game_num, name):
    if game_num == 1:
        return True if first_game(name) else False #возвращает True, если раунд выигран, иначе None
    elif game_num == 2:
        return True if second_game(name) else False
