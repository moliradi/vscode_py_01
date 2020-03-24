import random

#isEmpty = random.choice(['True', 'False'])
def ofRandom():
    for i in range(100):
        notEmpty = random.choice([True, False,False])
        if notEmpty:
            lis = random.choice([2,4])
            print('this is {0:^2} test ----  {1} ----  {2} -*'.format(i, notEmpty, lis))
            

arr = [[0, 3, 0, 0],
       [0, 2, 4, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 0]]

def of_Random(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                notEmpty = random.choice([True, False, False,False])
                if notEmpty:
                    arr[i][j] = random.choice([2,2,2,4])
if __name__ == '__main__':
    ofRandom()
    of_Random(arr)
    print(arr)