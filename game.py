from random import randint


def game_over(table):
    try:
        item = ' x '
        for c in range(0, 2):
            if table[0][0] == item and table[0][1] == item and table[0][2] == item:
                return True
            elif table[1][0] == item and table[1][1] == item and table[1][2] == item:
                return True
            elif table[2][0] == item and table[2][1] == item and table[2][2] == item:
                return True
            elif table[0][0] == item and table[1][0] == item and table[2][0] == item:
                return True
            elif table[0][1] == item and table[1][1] == item and table[2][1] == item:
                return True
            elif table[0][2] == item and table[1][2] == item and table[2][2] == item:
                return True
            elif table[0][0] == item and table[1][1] == item and table[2][2] == item:
                return True
            elif table[2][0] == item and table[1][1] == item and table[0][2] == item:
                return True
            item = ' o '
        voids = 9
        for line in range (0, 2):
            for colunm in range(0, 2):
                if not table[line][colunm] == '   ':
                    voids -= 1
        if voids == 0:
            return True
        return False
    except:
        print('There is something wrong!')


def player_decision(table, item):
    try:
        while True:
            line, column = 0, ''
            while not (line == 1 or line == 2 or line == 3):
                try:
                    line = int(input('Chosen line (──): '))
                except:
                    continue
            while not (column == 'A' or column == 'B' or column == 'C'):
                try:
                    column = input('Chosen colunm (|): ').strip().upper()[0]
                except:
                    continue
            line -= 1
            if column == 'A':
                column = 0
            elif column == 'B':
                column = 1
            elif column == 'C':
                column = 2
            if table[line][column] == '   ':
                table[line][column] = item
                return table
            else:
                print('Please, choose another...')
    except:
        print('There is something wrong!')


def computer_decision(table, item):
    try:
        test = item
        for counter in range(0, 2):
            for c in range(0, 3):
                if table[c][0] == '   ' and table[c][1] == test and table[c][2] == test:
                    table[c][0] = item
                    return table
                elif table[c][0] == test and table[c][1] == '   ' and table[c][2] == test:
                    table[c][1] = item
                    return table
                elif table[c][0] == test and table[c][1] == test and table[c][2] == '   ':
                    table[c][2] = item
                    return table
            for c in range(0, 3):
                if table[0][c] == '   ' and table[1][c] == test and table[2][c] == test:
                    table[0][c] = item
                    return table
                elif table[0][c] == test and table[1][c] == '   ' and table[2][c] == test:
                    table[1][c] = item
                    return table
                elif table[0][c] == test and table[1][c] == test and table[2][c] == '   ':
                    table[2][c] = item
                    return table
            for c in range(0, 2):
                if c == 0:
                    c1, c2, c3, c4, c5 = 0, 0, 1, 2, 2
                elif c == 1:
                    c1, c2, c3, c4, c5 = 0, 2, 1, 2, 0
                if table[c1][c2] == '   ' and table[c3][c3] == test and table[c4][c5] == test:
                    table[c1][c2] = item
                    return table
                elif table[c1][c2] == test and table[c3][c3] == '   ' and table[c4][c5] == test:
                    table[c3][c3] = item
                    return table
                elif table[c1][c2] == test and table[c3][c3] == test and table[c4][c5] == '   ':
                    table[c4][c5] = item
                    return table
            if item == ' x ':
                test = ' o '
            elif item == ' o ':
                test = ' x '
        while True:
            n1 = randint(0, 2)
            n2 = randint(0, 2)
            if table[n1][n2] == '   ':
                table[n1][n2] = item
                return table
    except:
        print('There is something wrong!')
