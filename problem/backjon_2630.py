import sys

board = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1]
]

def countBW(board):

    input_size = len(board) * len(board[0])

    if sum(map(sum, board)) == input_size:
        return 0, 1

    elif sum(map(sum, board)) == 0:
        return 1, 0

    div = int(len(board) / 2)

    result_b, result_w = 0, 0

    for i in range(2):
        for j in range(2):
            roi = [row[j*div:(j+1)*div] for row in board[i*div:(i+1)*div]]
            w, b = countBW(roi)
            result_b = result_b + b
            result_w = result_w + w

    return result_w, result_b

# test case 개수를 입력으로 받음.
for T in range(int(input())):
    board_size = int(input())
    board = []
    for row in range(board_size):
        board.append(list(map(int, input().split()))) 
        print(countBW(board))

