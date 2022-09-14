from random import randint


SIZE_N = 5
SIZE_M = 5


def generate_map(char_x, char_y, char_sign,
                 exit_x, exit_y,
                 size_n=SIZE_N, size_m=SIZE_M):
    
    world_map = ''

    for j in range(size_m):
        row = '|'

        for i in range(size_n):

            if char_x == i and char_y == j:
                row += f'{char_sign}|'
            elif exit_x == i and exit_y == j:
                row += 'O|'
            else:
                row += ' |'

        world_map += f'{row}\n'

    return world_map


def move(direction, x, y, size_n=SIZE_N, size_m=SIZE_M):
    if direction == 'u' and y > 0:
        y -= 1
    elif direction == 'd' and y < size_m - 1:
        y += 1
    elif direction == 'l' and x > 0:
        x -= 1
    elif direction == 'r' and x < size_n - 1:
        x += 1

    return x, y


char_x = randint(0, SIZE_N - 1)
char_y = randint(0, SIZE_M - 1)
char_sign = 'X'

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)

turns = 0

while True:

    world_map = ''
    win_condition = char_x == exit_x and char_y == exit_y

    if win_condition:
        char_sing = 'W'

    world_map = generate_map(char_x, char_y, char_sign,
                             exit_x, exit_y)
    print(world_map)

    if win_condition:
        print(f'You WON in {turns} turns!')
        break

    direction = input('Enter direction (u / d / l / r): ')

    char_x, char_y = move(direction, char_x, char_y)

    turns += 1

    
                      
