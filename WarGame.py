import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
from WG_Maps import uk_map

# Global Variables
BOARD_WIDTH = 34
BOARD_HEIGHT = 35
SQUARE_SIZE = int(min(768 / BOARD_HEIGHT, 1024 / BOARD_WIDTH, 150))
WIDTH = BOARD_WIDTH * SQUARE_SIZE
HEIGHT = (BOARD_HEIGHT + 1) * SQUARE_SIZE
PLAYER1 = 1
PLAYER2 = 2
CITIES = 2
POP_CENTRE = 1
WATER = -1
MOUNTAINS = -2

# Screen
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))


# Functions
def create_board(display=True, control=False, units=False):
    if not UK:
        if display:
            board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
            board[int(BOARD_HEIGHT / 2)][int(BOARD_HEIGHT / 2)] = CITIES
            board[int(BOARD_HEIGHT / 2)][BOARD_WIDTH - 1 - int(BOARD_HEIGHT / 2)] = CITIES
        if control:
            board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
            board[int(BOARD_HEIGHT / 2)][int(BOARD_HEIGHT / 2)] = PLAYER1
            board[int(BOARD_HEIGHT / 2)][BOARD_WIDTH - 1 - int(BOARD_HEIGHT / 2)] = PLAYER2
        if units:
            board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
            board[int(BOARD_HEIGHT / 2)][int(BOARD_HEIGHT / 2)] = 1
            board[int(BOARD_HEIGHT / 2)][BOARD_WIDTH - 1 - int(BOARD_HEIGHT / 2)] = 1

    if UK:
        if display:
            board = uk_map()
        if control:
            board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
            board[28][29] = PLAYER1
            board[21][20] = PLAYER2
        if units:
            board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
            board[28][29] = 1
            board[21][20] = 1
    return board


def draw_board(board):
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if board[r][c] == 0:
                pg.draw.rect(screen, (0, 255, 0), (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == CITIES:
                pg.draw.rect(screen, (255, 0, 255), (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == MOUNTAINS:
                pg.draw.rect(screen, (51, 17, 0), (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == WATER:
                pg.draw.rect(screen, (0, 213, 255), (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == POP_CENTRE:
                pg.draw.rect(screen, (255, 255, 0), (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pg.display.update()


def update_board(control_board, units_board):
    updates = []
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if control_board[r][c] == PLAYER1:
                updates.append([font.render(str(units_board[r][c]), True, (255, 0, 0)), r, c])
            if control_board[r][c] == PLAYER2:
                updates.append([font.render(str(units_board[r][c]), True, (0, 0, 255)), r, c])
    for update in updates:
        screen.blit(update[0], ((int(update[2]) * SQUARE_SIZE), int((update[1] + 5 / 4) * SQUARE_SIZE)))
    pg.display.update()


def units(player):
    units = 0
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if control_board[r][c] == player:
                if display_board[r][c] == MOUNTAINS:
                    units += 1 / 5
                if display_board[r][c] == 0:
                    units += 1 / 4
                if display_board[r][c] == POP_CENTRE:
                    units += 1 / 3
                if display_board[r][c] == CITIES:
                    units += 1
    unit = int(units)
    return unit


def isvalid_place(x, y, player):
    if control_board[x][y] == player:
        return True
    elif control_board[x][y] == 0:
        if y < BOARD_WIDTH - 1:
            if x == 0:
                if control_board[x][y + 1] == player or control_board[x][y - 1] == player or control_board[x + 1][
                    y] == player:
                    return True
            if x == BOARD_HEIGHT - 1:
                if control_board[x][y + 1] == player or control_board[x][y - 1] == player or control_board[x - 1][
                    y] == player:
                    return True
            else:
                if control_board[x - 1][y] == player or control_board[x + 1][y] == player:
                    return True
                elif control_board[x][y - 1] == player or control_board[x][y + 1] == player:
                    return True
        elif x == 0:
            if control_board[x][y] == player or control_board[x][y - 1] == player:
                return True
        elif x == BOARD_HEIGHT - 1:
            if control_board[x][y - 1] == player or control_board[x - 1][y] == player:
                return True
        else:
            if control_board[x][y - 1] == player or control_board[x - 1][y] == player or control_board[x + 1][
                y] == player:
                return True
    return False


def isconnected(player):
    cities = []
    connections = []
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if display_board[r][c] == CITIES and control_board[r][c] == player:
                cities.append([r, c])

    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if control_board[r][c] == player:
                connections.append([r, c])


def isvalid_attack(x, y, player):
    if player == PLAYER1:
        if control_board[x][y] == PLAYER2:
            if y < BOARD_HEIGHT - 1:
                if control_board[x][y - 1] == player:
                    return True
                elif control_board[x][y + 1] == player:
                    return True
            elif control_board[x][y - 1] == player:
                return True
            if x < BOARD_WIDTH - 1:
                if control_board[x + 1][y] == player:
                    return True
                elif control_board[x - 1][y] == player:
                    return True
            elif control_board[x - 1][y] == player:
                return True
    if player == PLAYER2:
        if y < BOARD_HEIGHT - 1:
            if control_board[x][y - 1] == player:
                return True
            elif control_board[x][y + 1] == player:
                return True
        elif control_board[x][y - 1] == player:
            return True
        if x < BOARD_WIDTH - 1:
            if control_board[x + 1][y] == player:
                return True
            elif control_board[x - 1][y] == player:
                return True
        elif control_board[x - 1][y] == player:
            return True
    return False


def battle(attacker, defender, display=False, tol=1):
    if turn == PLAYER1:
        if display_board[P1_POSx][P1_POSy] == WATER or display_board[P1_POSx][P1_POSy] == MOUNTAINS:
            tol = 2
    elif turn == PLAYER2:
        if display_board[P2_POSx][P2_POSy] == WATER or display_board[P2_POSx][P2_POSy] == MOUNTAINS:
            tol = 2

    def outcome(attacker, tol, maxunits=10):
        if attacker < 1:
            attacker = 1
        if attacker > maxunits:
            attacker = maxunits
        result = np.random.randint(attacker, size=2)
        if abs(result[0] - result[1]) < tol:
            return [0, result[0]]
        else:
            return [1, result[0]]

    if display:
        count = 1
        attack = [attacker]
        defence = [attacker]
    while defender != 0:
        fight = outcome(attacker, tol)
        if attacker < 1:
            attacker = 0
            if display:
                return print('Defenders won with ' + str(defender) + ' units left, the attackers have ' +
                             str(attacker) + ' units left in ' + str(count - 1) + ' turns'), graph
            else:
                return [attacker, defender]
        elif attacker == 1:
            if display:
                return print('Defenders won with ' + str(defender) + ' units left, the attackers have '
                             + str(attacker) + ' unit left in ' + str(count - 1) + ' turns'), graph
            else:
                return [attacker, defender]
        if fight[0] == 1:
            defender += -1
            if display:
                count += 1
                attack.append(attacker)
                defence.append(defender)
        elif fight[0] == 0:
            attacker += -fight[1] - 1
            if display:
                count += 1
                attack.append(attacker)
                defence.append(defender)
        if display:
            graph = plt.plot(np.arange(0, count, 1), attack, color='red')
            graph += plt.plot(np.arange(0, count, 1), defence, color='blue')
    if defender == 0:
        if display:
            return print('Attackers won with ' + str(attacker) + ' units left in ' + str(count - 1) + ' turns'), graph
        else:
            return [attacker, defender]


def get_attacker(x, y, player):
    if 0 < x < BOARD_WIDTH - 1 and y < BOARD_HEIGHT - 1:
        up = units_board[x - 1][y]
        right = units_board[x][y + 1]
        down = units_board[x + 1][y]
        left = units_board[x][y - 1]
        maks = np.max([up, right, down, left])
    elif y == BOARD_HEIGHT - 1:
        if x == 0:
            down = units_board[x + 1][y]
            left = units_board[x][y - 1]
            maks = np.max([down, left])
        elif x == BOARD_WIDTH - 1:
            up = units_board[x - 1][y]
            left = units_board[x][y - 1]
            maks = np.max([up, left])
        else:
            up = units_board[x - 1][y]
            down = units_board[x + 1][y]
            left = units_board[x][y - 1]
            maks = np.max([up, down, left])

    if maks == up:
        return [x - 1, y]
    elif maks == right:
        return [x, y + 1]
    elif maks == down:
        return [x + 1, y]
    elif maks == left:
        return [x, y - 1]


def win(player):
    opponent = PLAYER2
    if player == PLAYER2:
        opponent = PLAYER1
    city = 0
    city_player = 0
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if display_board[r][c] == CITIES:
                city += 1
                if control_board[r][c] == player:
                    city_player += 1
    if units(opponent) < 1 or 0 < city_player == city:
        return True
    return False


def scoreboard():
    p1score = font.render(str(units(PLAYER1)), True, (255, 0, 0))
    screen.blit(p1score, (int(BOARD_HEIGHT * 0.4 * SQUARE_SIZE), SQUARE_SIZE))
    verses = font.render('V', True, (0, 0, 0))
    screen.blit(verses, (int(BOARD_HEIGHT * 0.425 * SQUARE_SIZE), SQUARE_SIZE))
    p2score = font.render(str(units(PLAYER2)), True, (0, 0, 255))
    screen.blit(p2score, (int(BOARD_HEIGHT * 0.45 * SQUARE_SIZE), SQUARE_SIZE))


# Program
UK = True
font = pg.font.Font('freesansbold.ttf', int(0.64 * SQUARE_SIZE))
display_board = create_board()
# print('Display:', display_board)
control_board = create_board(control=True)
# print('Control:', control_board)
units_board = create_board(units=True)
# print('Units:', units_board)
draw_board(display_board)

game_over = False
turn = PLAYER1
P1_POSy = int(BOARD_HEIGHT / 2)
P1_POSx = int(BOARD_HEIGHT / 2)
P2_POSy = BOARD_WIDTH - 1 - int(BOARD_HEIGHT / 2)
P2_POSx = int(BOARD_HEIGHT / 2)
if UK:
    P1_POSy = 29
    P1_POSx = 28
    P2_POSy = 20
    P2_POSx = 21
P1_Units = units(PLAYER1)
P2_Units = units(PLAYER2)
DEBUG = False
# battle(100,100,True)
# plt.style.use('ggplot')
# plt.xlabel('Number of Turns')
# plt.ylabel('Units')
# plt.title('Battle Overview')
# plt.legend(['Attackers', 'Defenders'])
# plt.show()
# print('Units:', units_board[1][6])

while not game_over:
    update_board(control_board, units_board)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            game_over = True
        # Player 1
        if turn == PLAYER1:
            draw_board(display_board)
            pg.draw.rect(screen, (255, 0, 0),
                         (P1_POSy * SQUARE_SIZE, (P1_POSx + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                         int(SQUARE_SIZE / 10))
            turn_display1 = font.render('Player 1', True, (255, 0, 0))
            screen.blit(turn_display1, (0, SQUARE_SIZE))
            p1units_display = font.render('Units Remaining: ' + str(P1_Units), True, (0, 0, 0))
            screen.blit(p1units_display, (int(BOARD_HEIGHT * 0.75 * SQUARE_SIZE), SQUARE_SIZE))
            scoreboard()
            if DEBUG:
                # print('Player 1')
                pass
            # Board Movement
            if event.type == pg.KEYDOWN:
                if DEBUG:
                    print([P1_POSx, P1_POSy])
                if event.key == pg.K_RIGHT:
                    P1_POSy = (P1_POSy + 1) % BOARD_WIDTH
                    if DEBUG:
                        print('Right', [P1_POSx, P1_POSy])
                        # print(units_board)
                if event.key == pg.K_LEFT:
                    P1_POSy = (P1_POSy - 1) % BOARD_WIDTH
                    if DEBUG:
                        print('Left', [P1_POSx, P1_POSy])
                        # print(units_board)
                if event.key == pg.K_UP:
                    P1_POSx = (P1_POSx - 1) % BOARD_HEIGHT
                    if DEBUG:
                        print('Up', [P1_POSx, P1_POSy])
                        # print(units_board)
                if event.key == pg.K_DOWN:
                    P1_POSx = (P1_POSx + 1) % BOARD_HEIGHT
                    if DEBUG:
                        print('Down', [P1_POSx, P1_POSy])
                        # print(units_board)
                # Placing Units
                if event.key == pg.K_SPACE and isvalid_place(P1_POSx, P1_POSy, PLAYER1) and P1_Units > 0:
                    draw_board(display_board)
                    if control_board[P1_POSx][P1_POSy] == 0:
                        control_board[P1_POSx][P1_POSy] = PLAYER1
                    if control_board[P1_POSx][P1_POSy] != PLAYER2:
                        units_board[P1_POSx][P1_POSy] += 1
                        P1_Units -= 1
                    if DEBUG:
                        # print('Space', P1_Units)
                        print(units_board)
                # Attacking
                if event.key == pg.K_TAB:
                    if isvalid_attack(P1_POSx, P1_POSy, PLAYER1):
                        attacker = get_attacker(P1_POSx, P1_POSy, PLAYER1)
                        if DEBUG:
                            print('Attack Started')
                        if attacker == [P1_POSx, P1_POSy - 1]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P1_POSx][P1_POSy - 1], units_board[P1_POSx][P1_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P1_POSx][P1_POSy - 1] = result[0]
                                    control_board[P1_POSx][P1_POSy - 1] = 0
                                    units_board[P1_POSx][P1_POSy - 1] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P1_POSx][P1_POSy - 1] = result[0]
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P1_POSx][P1_POSy - 1] = 1
                                control_board[P1_POSx][P1_POSy] = PLAYER1
                                units_board[P1_POSx][P1_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                        elif attacker == [P1_POSx, P1_POSy + 1]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P1_POSx][P1_POSy + 1], units_board[P1_POSx][P1_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P1_POSx][P1_POSy + 1] = result[0]
                                    control_board[P1_POSx][P1_POSy + 1] = 0
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P1_POSx][P1_POSy + 1] = result[0]
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P1_POSx][P1_POSy + 1] = 1
                                control_board[P1_POSx][P1_POSy] = PLAYER1
                                units_board[P1_POSx][P1_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                        elif attacker == [P1_POSx - 1, P1_POSy]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P1_POSx - 1][P1_POSy], units_board[P1_POSx][P1_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P1_POSx - 1][P1_POSy] = result[0]
                                    control_board[P1_POSx - 1][P1_POSy] = 0
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P1_POSx - 1][P1_POSy] = result[0]
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P1_POSx - 1][P1_POSy] = 1
                                control_board[P1_POSx][P1_POSy] = PLAYER1
                                units_board[P1_POSx][P1_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                        elif attacker == [P1_POSx + 1, P1_POSy]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P1_POSx + 1][P1_POSy], units_board[P1_POSx][P1_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P1_POSx + 1][P1_POSy] = result[0]
                                    control_board[P1_POSx + 1][P1_POSy] = 0
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P1_POSx + 1][P1_POSy] = result[0]
                                    units_board[P1_POSx][P1_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P1_POSx + 1][P1_POSy] = 1
                                control_board[P1_POSx][P1_POSy] = PLAYER1
                                units_board[P1_POSx][P1_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                if event.key == pg.K_q:
                    turn = PLAYER2
                    P2_Units = units(PLAYER2)
                    if DEBUG:
                        print('P2_Units:', P2_Units)
                        print('Control', control_board)

        # Player 2
        if turn == PLAYER2:
            draw_board(display_board)
            pg.draw.rect(screen, (0, 0, 255),
                         (P2_POSy * SQUARE_SIZE, (P2_POSx + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                         int(SQUARE_SIZE / 10))
            turn_display2 = font.render('Player 2', True, (0, 0, 255))
            screen.blit(turn_display2, (0, SQUARE_SIZE))
            p2units_display = font.render('Units Remaining: ' + str(P2_Units), True, (0, 0, 0))
            screen.blit(p2units_display, (int(BOARD_HEIGHT * 0.75 * SQUARE_SIZE), SQUARE_SIZE))
            scoreboard()
            if DEBUG:
                # print('Player 2')
                pass
            # Board Movement
            if event.type == pg.KEYDOWN:
                if DEBUG:
                    print([P2_POSx, P2_POSy])
                if event.key == pg.K_RIGHT:
                    P2_POSy = (P2_POSy + 1) % BOARD_WIDTH
                    if DEBUG:
                        print('Right', [P2_POSx, P2_POSy])
                        # print(units_board)
                if event.key == pg.K_LEFT:
                    P2_POSy = (P2_POSy - 1) % BOARD_WIDTH
                    if DEBUG:
                        print('Left', [P2_POSx, P2_POSy])
                        # print(units_board)
                if event.key == pg.K_UP:
                    P2_POSx = (P2_POSx - 1) % BOARD_HEIGHT
                    if DEBUG:
                        print('Up', [P2_POSx, P2_POSy])
                        # print(units_board)
                if event.key == pg.K_DOWN:
                    P2_POSx = (P2_POSx + 1) % BOARD_HEIGHT
                    if DEBUG:
                        print('Down', [P2_POSx, P2_POSy])
                        # print(units_board)
                # Placing Units
                if event.key == pg.K_SPACE and isvalid_place(P2_POSx, P2_POSy, PLAYER2) and P2_Units > 0:
                    draw_board(display_board)
                    if control_board[P2_POSx][P2_POSy] == 0:
                        control_board[P2_POSx][P2_POSy] = PLAYER2
                    if control_board[P2_POSx][P2_POSy] != PLAYER1:
                        units_board[P2_POSx][P2_POSy] += 1
                        P2_Units -= 1
                    if DEBUG:
                        # print('Space', P2_Units)
                        print(units_board)
                # Attacking
                if event.key == pg.K_TAB:
                    if isvalid_attack(P2_POSx, P2_POSy, PLAYER2):
                        attacker = get_attacker(P2_POSx, P2_POSy, PLAYER2)
                        if DEBUG:
                            print('Attack Started')
                        if attacker == [P2_POSx, P2_POSy - 1]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P2_POSx][P2_POSy - 1], units_board[P2_POSx][P2_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P2_POSx][P2_POSy - 1] = result[0]
                                    control_board[P2_POSx][P2_POSy - 1] = 0
                                    units_board[P2_POSx][P2_POSy - 1] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P2_POSx][P2_POSy - 1] = result[0]
                                    units_board[P2_POSx][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P2_POSx][P2_POSy - 1] = 1
                                control_board[P2_POSx][P2_POSy] = PLAYER2
                                units_board[P2_POSx][P2_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                        elif attacker == [P2_POSx, P2_POSy + 1]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P2_POSx][P2_POSy + 1], units_board[P2_POSx][P2_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P2_POSx][P2_POSy + 1] = result[0]
                                    control_board[P2_POSx][P2_POSy + 1] = 0
                                    units_board[P2_POSx][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P2_POSx][P2_POSy + 1] = result[0]
                                    units_board[P2_POSx][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P2_POSx][P2_POSy + 1] = 1
                                control_board[P2_POSx][P2_POSy] = PLAYER2
                                units_board[P2_POSx][P2_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                        elif attacker == [P2_POSx - 1, P2_POSy]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P2_POSx - 1][P2_POSy], units_board[P2_POSx][P2_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P2_POSx - 1][P2_POSy] = result[0]
                                    control_board[P2_POSx - 1][P2_POSy] = 0
                                    units_board[P2_POSx - 1][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P2_POSx - 1][P2_POSy] = result[0]
                                    units_board[P2_POSx][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P2_POSx - 1][P2_POSy] = 1
                                control_board[P2_POSx][P2_POSy] = PLAYER2
                                units_board[P2_POSx][P2_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                        elif attacker == [P2_POSx + 1, P2_POSy]:
                            if DEBUG:
                                print('Battle Started')
                            result = battle(units_board[P2_POSx + 1][P2_POSy], units_board[P2_POSx][P2_POSy])
                            if result[1] != 0:
                                if result[0] == 0:
                                    units_board[P2_POSx + 1][P2_POSy] = result[0]
                                    control_board[P2_POSx + 1][P2_POSy] = 0
                                    units_board[P2_POSx][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                                else:
                                    units_board[P2_POSx + 1][P2_POSy] = result[0]
                                    units_board[P2_POSx][P2_POSy] = result[1]
                                    if DEBUG:
                                        print('Attack finished')
                            else:
                                units_board[P2_POSx + 1][P2_POSy] = 1
                                control_board[P2_POSx][P2_POSy] = PLAYER2
                                units_board[P2_POSx][P2_POSy] = result[0] - 1
                                if DEBUG:
                                    print('Attack finished')
                if event.key == pg.K_w:
                    turn = PLAYER1
                    P1_Units = units(PLAYER1)
                    if DEBUG:
                        print('P1_Units:', P1_Units)
                        print('Control', control_board)
    # Win Conditions
    if win(PLAYER1):
        print('Player 1 Wins !')
        pg.time.wait(1000)
        game_over = True
    if win(PLAYER2):
        print('Player 2 Wins!')
        pg.time.wait(1000)
        game_over = True
    pg.display.update()
