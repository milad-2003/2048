import random


table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


print("""Press 'A' to MOVE LEFT
Press 'S' to MOVE DOWN
Press 'D' to MOVE RIGHT
Press 'W' to MOVE UP""")


def add_new_2():
    row = random.randint(0, 3)
    column = random.randint(0, 3)
    while 0 not in table[row]:
        row = random.randint(0, 3)
    while table[row][column] != 0:
        column = random.randint(0, 3)
    table[row][column] = 2


def status():
    for i in range(0, 4):
        for j in range(0, 4):
            if table[i][j] == 2048:
                return "You won!"
            
    for i in range(0, 4):
        for j in range(0, 4):
            if table[i][j] == 0:
                return "Game not over yet..."

    for i in range(0, 4):
        for j in range(1, 4):
            if table[i][j - 1] == table[i][j]:
                return "Game not over yet..."

    for i in range(1, 4):
        for j in range(0, 4):

            if table[i - 1][j] == table[i][j]:
                return "Game not over yet..."

    return "Game over!"

