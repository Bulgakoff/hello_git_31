import random


def main():
    min_n = 1
    max_n = 50
    puzzle_num = random.randint(min_n, max_n)
    game_guess(puzzle_num, min_n, max_n)


def game_guess(p_n, minn, maxx):
    attempts = 0
    print(p_n)
    guess_num = None

    while cond(attempts, guess_num, p_n, minn, maxx):
        guess_num = int(input('Введите свой ответ : '))
        attempts += 1
        if p_n < guess_num:
            maxx = guess_num - 1
            print(f'attempts № {attempts} ')
            print(f'Вы ввели больше и теперь ваше число не дальше к концу {maxx}б в диапазоне oот {minn} до {maxx}')
        elif p_n > guess_num:
            minn = guess_num + 1
            print(f'attempts № {attempts} ')
            print(f'Вы ввели меньше  и теперь ваше число не дальше к началу  {minn} в диапазоне oот {minn} до {maxx}')
        elif p_n == guess_num:
            print(f'attempts № {attempts} ')
            print(f'Вы угадали!!! за {attempts} попыток')
            break

    else:
        print(f'Вы потратили все {attempts} попыток - ПРОИРЫШ!!!')

    print('GAME OVER')


def cond(a, g, p, mi, ma):
    return a < 6 and g != p


main()
