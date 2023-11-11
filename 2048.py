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


def zeros_to_right(arr):
    number_of_zeros = arr.count(0)
    for i in range(0, number_of_zeros):
        arr.remove(0)
        arr.append(0)


def zeros_to_left(arr):
    number_of_zeros = arr.count(0)
    for i in range(0, number_of_zeros):
        arr.remove(0)
    for i in range(0, number_of_zeros):
        arr.insert(0, 0)


def zeros_to_bottom(arr, column):
    temp = []
    for j in range(len(arr)):
        temp.append(arr[j][column])
    zeros_to_right(temp)
    for j in range(len(arr)):
        arr[j][column] = temp[j]
    

def zeros_to_top(arr, column):
    temp = []
    for j in range(len(arr)):
        temp.append(arr[j][column])
    zeros_to_left(temp)
    for j in range(len(arr)):
        arr[j][column] = temp[j]


def move_right(arr):
    for i in range(len(arr)):
        zeros_to_left(arr[i])
        for j in range(len(arr) - 1, 0, -1):
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] *= 2
                arr[i][j - 1] = 0
                zeros_to_left(arr[i])


def move_left(arr):
    for i in range(len(arr)):
        zeros_to_right(arr[i])
        for j in range(len(arr) - 1):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] *= 2
                arr[i][j + 1] = 0
                zeros_to_right(arr[i])


def move_down(arr):
    for i in range(len(arr)):
        zeros_to_top(arr, i)
        for j in range(len(arr) - 1, 0, -1):
            if arr[j][i] == arr[j - 1][i]:
                arr[j][i] *= 2
                arr[j - 1][i] = 0
                zeros_to_top(arr, i)


def move_up(arr):
    for i in range(len(arr)):
        zeros_to_bottom(arr, i)
        for j in range(len(arr) - 1):
            if arr[j][i] == arr[j + 1][i]:
                arr[j][i] *= 2
                arr[j + 1][i] = 0
                zeros_to_bottom(arr, i)


