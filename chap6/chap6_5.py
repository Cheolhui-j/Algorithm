import sys

# 가능한 블럭의 경우의 수는 4가지. 이 경우들에 대해 모형화를 시킴.
block = [
    [(0,0), (1, 0), (0, 1)],
    [(0,0), (0, 1), (1, 1)],
    [(0,0), (1, 0), (1, 1)],
    [(0,0), (1, 0), (1, -1)]
    ]

# 각 타일이 가능한지 여부를 검사.
# 보드를 벗어나는지, 이미 칠해진 곳을 덮진 않는지
def checkcover(y, x, currentblock, board, a):
    check = True
    for order in range(len(currentblock)):
        set_y = y + currentblock[order][0]
        set_x = x + currentblock[order][1]
        if set_y < 0 or set_y > len(board) - 1 or set_x < 0 or set_x > len(board[0]) - 1:
            check = False
        # 보드를 덮음.
        else :
            board[set_y][set_x] = board[set_y][set_x] + a
            if board[set_y][set_x] > 1:
                check = False
    return check

def coverboard(rows, cols, board):
    cand_x = -1
    cand_y = -1
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                cand_y = row
                cand_x = col
                break 
        if cand_y != -1 :
            break

    if cand_x == -1 or cand_y == -1:
        return 1

    ret = 0
    for i in range(len(block)):
        if checkcover(cand_y, cand_x, block[i], board, 1):
            ret = ret + coverboard(rows, cols, board)
        checkcover(cand_y, cand_x, block[i], board, -1)
    return ret


# test case 개수를 입력으로 받음.
for T in range(int(input())):
    rows, cols = map(int, input().split())
    board = []
    for row in range(rows):
        board.append(list(map(int, input().split()))) 
    print(coverboard(rows, cols, board))