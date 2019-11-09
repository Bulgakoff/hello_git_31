
def main():
    game_china(20)

def game_china(sticks):

    player_turn = 1

    while not end_of_game(sticks):  # (sticks)argument
        # while sticks != 0:
        print(f'как много палочек вы взяли? осталось {sticks} палочки: \n ')

        taken = int(input())
        if range_take(taken):  # (taken)argument

            # if taken > 3 or taken < 1:
            print(f'Вы ввели неправильно {taken} - нужно от 1 до 3')
            continue  # go to while
        else:
            sticks -= taken  # остаток
            print(f'отстаток {sticks} палочки ')
        # нужно проверить сколько осталось
        if end_of_game(sticks):  # (sticks)argument

            # if sticks <= 0:
            print(f'Play finish нет больше палочек и игрок  {player_turn} проиграл ')
        else:
            player_turn = turn_players(player_turn)
            # player_turn = 1 if player_turn == 2 else 2


def end_of_game(f):  # param прораб
    return f <= 0


def range_take(f):  # param прораб
    return f > 3 or f < 1


def turn_players(f):  # param прораб
    return 1 if f == 2 else 2




main()
