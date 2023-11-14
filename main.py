from random import randint
from msvcrt import getch
import move


table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

table_copy = []

score = 0


print("""
Press 'A' to MOVE LEFT
Press 'S' to MOVE DOWN
Press 'D' to MOVE RIGHT
Press 'W' to MOVE UP
Press 'Q' to exit
""")


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
        print("You can only select 'A', 'S', 'D' or 'W': \nPress 'Q' to exit: ")
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

    print(f"Score: {score}")

    for i in table:
        print("\n--------------------------------")
        for j in i:
            if j:
                print(j, "\t", end="")
            else:
                print("", "\t", end="")
    print("\n================================\n")
    
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

print(f"Game over!\nScore: {score}")
