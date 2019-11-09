import random
<<<<<<< HEAD
#надо добавить коммент
puzzle_num = random.randint(1, 50)
=======

min_n = 1
max_n = 50
puzzle_num = random.randint(min_n, max_n)
>>>>>>> f56dd1f43f334d1b6b2976452ca45c6231f0b8ca


def main():
    game_guess(puzzle_num)


def game_guess(p_n):
    attempts = 0
    print(p_n)
    guess_num = None

    while cond(attempts, guess_num, p_n):
        guess_num = int(input('Введите свой ответ : '))
        attempts += 1
        if p_n < guess_num:
            print(f'attempts № {attempts} ')
            print('Вы ввели больше ')
        elif p_n > guess_num:
            print(f'attempts № {attempts} ')
            print('Вы ввели меньше ')
        elif p_n == guess_num:
            print(f'attempts № {attempts} ')
            print(f'Вы угадали!!! за {attempts} попыток')
            break

    else:
        print(f'Вы потратили все {attempts} попыток - ПРОИРЫШ!!!')

    print('GAME OVER')


def cond(a, g, p):
    return a < 6 and g != p


main()
