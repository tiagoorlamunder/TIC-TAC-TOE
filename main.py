from os import system
from game import *
from show import *


while True:
    system('cls')
    print('\033[1;97m' + '>>> TIC-TAC-TOE <<<' + '\033[0;0m')
    print()
    print('1. Play with friend')
    print('2. Play with computer')
    print('3. Just leave')
    option = int(input('Your option: '))
    if option == 1:
        table = [['   ', '   ', '   '],
                 ['   ', '   ', '   '],
                 ['   ', '   ', '   ']]
        print()
        player1 = player2 = ''
        while player1 == '':
            player1 = input('First player name: ').strip().capitalize()
        while player2 == '':
            player2 = input('Second player name: ').strip().capitalize()
            if player2 == player1:
                print('Please, choose another...')
                player2 = ''
        for c in range(0, 9):
            if c % 2 == 0:
                player, item = player1, ' x '
            else:
                player, item = player2, ' o '
            system('cls')
            show(table)
            line()
            print(f'Play, {player}!')
            table = player_decision(table, item)
            if game_over(table) == True:
                system('cls')
                show_end(table)
                line()
                print(f'The player {player} won!!!')
                print()
                pause = input('Click ENTER to continue...')
                break
    elif option == 2:
        table = [['   ', '   ', '   '],
                ['   ', '   ', '   '],
                ['   ', '   ', '   ']]
        print()
        player = input('Player name: ').strip().capitalize()
        item = ' x '
        while True:
            option = input(f'Do you want to start, {player}? (Y/N) ').strip().upper()[0]
            if option == 'Y':
                system('cls')
                show(table)
                line()
                print(f'Play, {player}!')
                table = player_decision(table, item)
                item = ' o '
                break
            elif option == 'N':
                break
            else:
                print('Please, choose another...')
        while True:
            system('cls')
            show(table)
            simulate_loading()
            table = computer_decision(table, item)
            if game_over(table) == True:
                system('cls')
                show_end(table)
                line()
                print(f'The computer won!!!')
                print()
                pause = input('Click ENTER to continue...')
                break
            system('cls')
            show(table)
            line()
            if item == ' x ':
                item = ' o '
            elif item == ' o ':
                item = ' x '
            print(f'Play, {player}!')
            table = player_decision(table, item)
            if game_over(table) == True:
                system('cls')
                show_end(table)
                line()
                print(f'The player {player} won!!!')
                print()
                pause = input('Click ENTER to continue...')
                break
            if item == ' x ':
                item = ' o '
            elif item == ' o ':
                item = ' x '
    else:
        print('Thank you for everything!')
        break
