N, M = map(int, input().split())

matrick_A = []
matrick_B = []

# 행렬 A 값 입력
for row in range(N):
    matrick_A.append(list(map(int, input().split())))

# 행렬 B 값 입력
for row in range(N):
    matrick_B.append(list(map(int, input().split())))

# 행렬 A,B 합치기
for row in range(N):
    for col in range(M):
        print(matrick_A[row][col] + matrick_B[row][col], end=" ")
    print()