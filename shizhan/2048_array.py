
arr = [[0, 3, 0, 0],
       [0, 2, 4, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0]]

print('*-----*-----*-----*-----*')
print('|{:^5}|{:^5}|{:^5}|{:^5}|'.format(arr[0][0], arr[0][1], arr[0][2], arr[0][3]))
print('*-----*-----*-----*-----*')

print('=========================')

def print_arr(arr):
    line01 = '*-----*-----*-----*-----*'
    print(line01)
    for i in range(4):
        print('|{:^5}|{:^5}|{:^5}|{:^5}|'.format(arr[i][0], arr[i][1], arr[i][2], arr[i][3]))
        print(line01)

print_arr(arr)