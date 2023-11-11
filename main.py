from random import randint
import move


table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


print("""
Press 'A' to MOVE LEFT
Press 'S' to MOVE DOWN
Press 'D' to MOVE RIGHT
Press 'W' to MOVE UP
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
    input_list = ['A', 'S', 'D', 'W', 'a', 's', 'd', 'w']
    user_input = input()
    while user_input not in input_list:
        print("You can only select 'A', 'S', 'D' or 'W': ")
        user_input = input()

    return user_input.lower()


while not game_over(table):

    add_new_2(table)

    for i in table:
        for j in i:
            print(j, "\t", end="")
        print("")
    print("\n================================\n")
        
    match user():
        case "a":
            move.left(table)
        case "s":
            move.down(table)
        case "d":
            move.right(table)
        case "w":
            move.up(table)

print("Game over!")
