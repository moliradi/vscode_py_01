def a_Move(arr):
    for i in range(4):
        for j in range(3):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] = 2 * arr[i][j]
                arr[i][j + 1] = 0

    for i in range(4):
        for j in range(1,4):
            if arr[i][j] != 0:
                temp = j
                while temp > 0 and arr[i][temp - 1] == 0:
                    temp = temp - 1
                if j != temp:
                    arr[i][temp] = arr[i][j]
                    arr[i][j] = 0

def print_arr(arr):
    line01 = '*-----*-----*-----*-----*'
    print(line01)
    for i in range(4):
        print('|{0:^5}|{1:^5}|{2:^5}|{3:^5}|'.format(arr[i][0], arr[i][1], arr[i][2], arr[i][3]))
        print(line01)

arr = [[0, 3, 0, 0],
       [4, 2, 0, 2],
       [0, 1, 1, 0],
       [16, 0, 2, 0]]

print_arr(arr)
a_Move(arr)
print_arr(arr)

