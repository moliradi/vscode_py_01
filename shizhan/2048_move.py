import random
list01 = [0, 2, 0, 2]
list02 = [4, 2, 0, 2]
list03 = [16, 16, 2, 0]
list04 = [2, 2, 2, 2]
list05 = [4, 4, 8, 0]


def leftMove(list):
    for i in range(0, 3):
        if list[i] != 0:
            if list[i + 1] == list[i]:
                list[i] = 2 * list[i]
                list[i + 1] = 0
    
    list2 = [0, 0, 0, 0]
    temp = 0
    for i in range(0, 4):
        if list[i] != 0:
            list2[temp] = list[i]
            temp = temp + 1

    for i in range(4):
        list[i] = list2[i]
        
    return list

text = leftMove(list02)
print(text)


arr = [[0, 3, 0, 0],
       [0, 2, 4, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 0]]
#从左向右，依次叠加
def left_Count(arr):
    for i in range(4):
        for j in range(3):
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] = 2 * arr[i][j]
                arr[i][j + 1] = 0
                
#从右向左，
def left_Move(arr):
    for i in range(4):
        for j in range(1,4):
            if arr[i][j] != 0:
                temp = j
                while temp > 0 and arr[i][temp - 1] == 0:
                    temp = temp - 1
                arr[i][temp] = arr[i][j]
                arr[i][j] = 0

left_Count(arr)
#left_Move(arr)

print(arr)
#cdcdscdscds

