import sys

board = [
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [0, 0, 0, 1, 1, 1, -1, -1, -1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, -1, 0, 1, -1, 0, 1, -1],
    [0, -1, 1, 0, 1, -1, 0, 1, -1],
    [0, 1, -1, 1, 0, -1, 0, 1, -1]
]

def list_sum(a, abs_0 = False):
    res_sum = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if abs_0:
                res_sum = res_sum + abs(a[i][j])
            else :
                res_sum = res_sum + a[i][j]
    return res_sum

def checkboared(board):

    if not board:
        return 0, 0, 0

    input_size = len(board) * len(board[0])

    if list_sum(board) == -input_size:
        return 1, 0, 0

    elif list_sum(board, True) == 0:
        return 0, 1, 0
    
    elif list_sum(board) == input_size:
        return 0, 0, 1

    div = int(len(board) / 3)

    out_m1 = 0 # -1
    out_0 = 0 # 0
    out_p1 = 0 # 1

    for i in range(3):
        for j in range(3):
            roi = [row[j*div:(j+1)*div] for row in board[i*div:(i+1)*div]]
            result_m1, result_0, result_p1 = checkboared(roi)
            out_m1 = out_m1 + result_m1
            out_0 = out_0 + result_0
            out_p1 = out_p1 + result_p1

    return out_m1, out_0, out_p1

# test case 개수를 입력으로 받음.

board_size = int(input())
board = []
for row in range(board_size):
    board.append(list(map(int, input().split()))) 
print(checkboared(board)[0])
print(checkboared(board)[1])
print(checkboared(board)[2])