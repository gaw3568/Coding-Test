import sys
N,M = map(int, sys.stdin.readline().split())
board = []
new_board = []

for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

# 최소로 자르는 크기는 8X8 이므로 N-7, M-7 의 범위를 두고 반복문을 돌려준다.
for i in range(N-7):
    for j in range(M-7):
        black_f = 0
        white_f = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "W":
                        white_f += 1
                    if board[a][b] != "B":
                        black_f += 1
                else:
                    if board[a][b] != "B":
                        white_f += 1
                    if board[a][b] != "W":
                        black_f += 1
        new_board.append(white_f)
        new_board.append(black_f)
print(min(new_board))