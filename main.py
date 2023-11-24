from random import randint
from msvcrt import getch
import move
from os import system as command
from platform import system as os


table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

table_copy = []

score = 0

color_dict = {
    2: (0, 41),
    4: (0, 42),
    8: (0, 43),
    16: (0, 44),
    32: (0, 45),
    64: (0, 46),
    128: (0, 47),
    256: (1, 41),
    512: (1, 42),
    1024: (1, 43),
    2048: (1, 44),
    4096: (1, 45),
    8192: (1, 46),
    16384: (1, 47),
    32768: (7, 41),
    65536: (7, 42),
    131072: (7, 43),
    262144: (7, 44),
    524288: (7, 45),
    1048576: (7, 46),
    2097152: (7, 47)
}


def add_new_2(arr):
    for i in range(len(arr)):
        if 0 in arr[i]:
            row = randint(0, 3)
            column = randint(0, 3)
            while 0 not in arr[row]:
                row = randint(0, 3)
            while arr[row][column] != 0:
                column = randint(0, 3)
            arr[row][column] = 2
            break


def game_over(arr):
    for i in range(0, 4):
        for j in range(0, 4):
            if arr[i][j] == 0:
                return False

    for i in range(0, 4):
        for j in range(1, 4):
            if arr[i][j - 1] == arr[i][j]:
                return False

    for i in range(1, 4):
        for j in range(0, 4):

            if arr[i - 1][j] == arr[i][j]:
                return False

    return True


def user():
    input_list = ['A', 'S', 'D', 'W', 'Q', 'a', 's', 'd', 'w', 'q']
    user_input = str(getch())[2]
    while user_input not in input_list:
        print("\033[1;31;40mYou can only select 'A', 'S', 'D' or 'W': \nPress 'Q' to exit: ")
        user_input = str(getch())[2]

    return user_input.lower()


def copy(arr):
    new_arr = []
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr)):
            temp.append(arr[i][j])
        new_arr.append(temp)
    
    return new_arr


while not game_over(table):

    if table != table_copy:
        add_new_2(table)

    if os() == "Windows":
        command("cls")
    else:
        command("clear")
    
    print("""\033[0;32;40m
Press 'A', 'S', 'D' or 'W' to move
Press 'Q' to exit
""")

    print(f"\033[1;34;40mScore: {score}")

    for i in table:
        print("\033[0;37;40m\n--------------------------------")
        for j in i:
            if j:
                print(f"\033[{color_dict[j][0]};37;{color_dict[j][1]}m{j}", "\033[0;37;40m\t", end="")
            else:
                print("", "\t", end="")
    print("\033[1;35;40m\n================================\n")
    
    # Making a copy of the table to know if it was changed in the next iteration
    table_copy = copy(table)

    match user():
        case "a":
            score += move.left(table)
        case "s":
            score += move.down(table)
        case "d":
            score += move.right(table)
        case "w":
            score += move.up(table)
        case "q":
            break

print(f"\033[0;33;40mGame over!\nScore: {score}")
