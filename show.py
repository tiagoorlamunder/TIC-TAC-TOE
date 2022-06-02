from time import sleep


def show(table):
    try:
        MAGENTA = '\033[1;95m'
        GRAY = '\033[1;47m'
        RESET = '\033[1;m'
        print(GRAY + '     A   B   C     ' + RESET)
        print(GRAY + '   ' + RESET + MAGENTA + '┌───────────┐' + GRAY + '   ' + RESET)
        print(GRAY + ' 1 ' + RESET + MAGENTA + '│' + RESET + table[0][0] + '│' + table[0][1] + '│' + table[0][2] + MAGENTA + '│' + GRAY + '   ' + RESET)
        print(GRAY + '   ' + RESET + MAGENTA + '│' + RESET + '───┼───┼───' + MAGENTA + '│' + GRAY + '   ' + RESET)
        print(GRAY + ' 2 ' + RESET + MAGENTA + '│' + RESET + table[1][0] + '│' + table[1][1] + '│' + table[1][2] + MAGENTA + '│' + GRAY + '   ' + RESET)
        print(GRAY + '   ' + RESET + MAGENTA + '│' + RESET + '───┼───┼───' + MAGENTA + '│' + GRAY + '   ' + RESET)
        print(GRAY + ' 3 ' + RESET + MAGENTA + '│' + RESET + table[2][0] + '│' + table[2][1] + '│' + table[2][2] + MAGENTA + '│' + GRAY + '   ' + RESET)
        print(GRAY + '   ' + RESET + MAGENTA + '└───────────┘' + GRAY + '   ' + RESET)
        print(GRAY + 19 * ' ' + RESET)
    except:
        print('There is something wrong!')


def show_end(table):
    try:
        RED = '\033[1;31m'
        RESET = '\033[1;m'
        item = ' x '
        for c in range(0, 2):
            if table[0][0] == item and table[0][1] == item and table[0][2] == item:
                table[0][0] = table[0][1] = table[0][2] = RED + item + RESET
                show(table)
            elif table[1][0] == item and table[1][1] == item and table[1][2] == item:
                table[1][0] = table[1][1] = table[1][2] = RED + item + RESET
                show(table)
            elif table[2][0] == item and table[2][1] == item and table[2][2] == item:
                table[2][0] = table[2][1] = table[2][2] = RED + item + RESET
                show(table)
            elif table[0][0] == item and table[1][0] == item and table[2][0] == item:
                table[0][0] = table[1][0] = table[2][0] = RED + item + RESET
                show(table)
            elif table[0][1] == item and table[1][1] == item and table[2][1] == item:
                table[0][1] = table[1][1] = table[2][1] = RED + item + RESET
                show(table)
            elif table[0][2] == item and table[1][2] == item and table[2][2] == item:
                table[0][2] = table[1][2] = table[2][2] = RED + item + RESET
                show(table)
            elif table[0][0] == item and table[1][1] == item and table[2][2] == item:
                table[0][0] = table[1][1] = table[2][2] = RED + item + RESET
                show(table)
            elif table[2][0] == item and table[1][1] == item and table[0][2] == item:
                table[2][0] = table[1][1] = table[0][2] = RED + item + RESET
                show(table)
            item = ' o '
    except:
        print('There is something wrong!')


def simulate_loading():
    print()
    for character in 'The computer is loading...':
        print(character, end = '', flush = True)
        sleep(0.02)
        if character in 'ng...':
            sleep(0.2)
    print()
    print()


def line():
    print()
    for c in range(0, 19):
        print('=', end = '', flush=True)
        sleep(0.04)
    print()
    print()
