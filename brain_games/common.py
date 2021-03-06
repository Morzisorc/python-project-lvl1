import prompt
from brain_games.games.fifth import fifth_game, fifth_task
from brain_games.games.first import first_game, first_task
from brain_games.games.forth import forth_game, forth_task
from brain_games.games.second import second_game, second_task
from brain_games.games.third import third_game, third_task


def welcome():
    print('Welcome to the Brain Games!')


def say_hello():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name


def start_game(game_num):
    welcome()  # приветствует игрока
    name = say_hello()  # узнет и запоминает имя, здоровается
    give_task(game_num)
    count = 0
    while count < 3:
        # запуск раунда и проверка, выигран ли он
        if is_round_won(game_num, name):
            count += 1
            print('Correct!')
        else:
            return True

        # проверка на 3 победы
        if count == 3:
            return print(f'Congratulations, {name}!')


def give_task(game_num):
    if game_num == 1:
        first_task()
    elif game_num == 2:
        second_task()
    elif game_num == 3:
        third_task()
    elif game_num == 4:
        forth_task()
    elif game_num == 5:
        fifth_task()


def is_round_won(game_num, name):
    if game_num == 1:
        return bool(first_game(name))  # проверяет, выигран ли раунд
    elif game_num == 2:
        return bool(second_game(name))
    elif game_num == 3:
        return bool(third_game(name))
    elif game_num == 4:
        return bool(forth_game(name))
    elif game_num == 5:
        return bool(fifth_game(name))
