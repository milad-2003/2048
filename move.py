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


def right(arr):
    for i in range(len(arr)):
        zeros_to_left(arr[i])
        for j in range(len(arr) - 1, 0, -1):
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] *= 2
                arr[i][j - 1] = 0
                zeros_to_left(arr[i])


def left(arr):
    for i in range(len(arr)):
        zeros_to_right(arr[i])
        for j in range(len(arr) - 1):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] *= 2
                arr[i][j + 1] = 0
                zeros_to_right(arr[i])


def down(arr):
    for i in range(len(arr)):
        zeros_to_top(arr, i)
        for j in range(len(arr) - 1, 0, -1):
            if arr[j][i] == arr[j - 1][i]:
                arr[j][i] *= 2
                arr[j - 1][i] = 0
                zeros_to_top(arr, i)


def up(arr):
    for i in range(len(arr)):
        zeros_to_bottom(arr, i)
        for j in range(len(arr) - 1):
            if arr[j][i] == arr[j + 1][i]:
                arr[j][i] *= 2
                arr[j + 1][i] = 0
                zeros_to_bottom(arr, i)

