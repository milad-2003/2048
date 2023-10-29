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

