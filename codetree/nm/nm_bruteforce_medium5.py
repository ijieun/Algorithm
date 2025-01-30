board = [list(map(int, input().split())) for _ in range(19)]
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],...

def find_winner():
    for i in range(19):
        for j in range(19):
            # 가로 한줄 
            if j<15:
                if board[i][j] != 0 and board[i][j]==board[i][j+1] and board[i][j+1] == board[i][j+2] and \
                board[i][j+2] == board[i][j+3] and board[i][j+3] == board[i][j+4]:
                    return board[i][j],(i+1, j+3)
            # 세로 한줄
            if i<15:
                if board[i][j] != 0 and board[i+1][j]==board[i][j] and board[i+2][j] == board[i+1][j] and \
                board[i+2][j] == board[i+3][j] and board[i+3][j] == board[i+4][j]:
                    return board[i][j],(i+3, j+1)
            # 아래 대각선 한줄 
            if i<15 and j<15:
                if board[i][j] != 0 and board[i+1][j+1]==board[i][j] and board[i+2][j+2] == board[i+1][j+1] and \
                board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] == board[i+4][j+4]:
                    return board[i][j],(i+3, j+3)
            # 윗 대각선 한줄 
            if i<15 and j>3:
                if board[i][j] != 0 and board[i+1][j-1]==board[i][j] and board[i+2][j-2] == board[i+1][j-1] and \
                board[i+2][j-2] == board[i+3][j-3] and board[i+3][j-3] == board[i+4][j-4]:
                    return board[i][j],(i+3, j-1)
    return 0
if find_winner()==0:
    print(0)
else:
    print(find_winner()[0])
    print(find_winner()[1][0], end=" ")
    print(find_winner()[1][1])