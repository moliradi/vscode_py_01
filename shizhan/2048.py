import random

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

def d_Move(arr):
    for i in range(4):
        for j in range(3, 0, -1):
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] = 2 * arr[i][j]
                arr[i][j - 1] = 0

    for i in range(4):
        for j in range(2, -1, -1):
            if arr[i][j] != 0:
                temp = j
                while temp < 3 and arr[i][temp + 1] == 0:
                    temp = temp + 1
                if j != temp:
                    arr[i][temp] = arr[i][j]
                    arr[i][j] = 0

def w_Move(arr):
    for j in range(4):
        for i in range(3):
            if arr[i][j] == arr[i + 1][j]:
                arr[i][j] = 2 * arr[i][j]
                arr[i + 1][j] = 0
                
    for j in range(4):
        for i in range(1, 4):
            if arr[i][j] != 0:
                temp = i
                while temp > 0 and arr[temp - 1][j] == 0:
                    temp = temp - 1
                if i != temp:
                    arr[temp][j] = arr[i][j]
                    arr[i][j] = 0

def s_Move(arr):
    for j in range(4):
        for i in range(3, 0, -1):
            if arr[i][j] == arr[i - 1][j]:
                arr[i][j] = 2 * arr[i][j]
                arr[i - 1][j] = 0

    for j in range(4):
        for i in range(2, -1, -1):
            if arr[i][j] != 0:
                temp = i
                while temp < 3 and arr[temp + 1][j] == 0:
                    temp = temp + 1
                if i != temp:
                    arr[temp][j] = arr[i][j]
                    arr[i][j] = 0

def of_Random(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                notEmpty = random.choice([True, False, False, False, False, False, False])
                if notEmpty:
                    arr[i][j] = random.choice([2, 2, 2, 4])
                    
def print_arr(arr):
    line01 = '*-----*-----*-----*-----*'
    print(line01)
    for i in range(4):
        print('|{0:^5}|{1:^5}|{2:^5}|{3:^5}|'.format(arr[i][0], arr[i][1], arr[i][2], arr[i][3]))
        print(line01)

def choice_Direction(arr, com):
    if com in ['w', 'a', 's', 'd']:
        if com == 'w':
            w_Move(arr)
        elif com == 'a':
            a_Move(arr)
        elif com == 's':
            s_Move(arr)
        else:
            d_Move(arr)

def test_Over(arr, ifOver):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 2048:
                ifOver = True
    
    return ifOver

def one_Game(arr):
    #print_arr(arr)
    com = input('please enter a commend in 【w,a,s,d】:')
    choice_Direction(arr, com)
    of_Random(arr)
    print_arr(arr)

def main():
    arr = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
    of_Random(arr)
    print_arr(arr)
    ifOver = False
    while not ifOver:
        one_Game(arr)
        test_Over(arr, ifOver)

if __name__ == '__main__':
    main()