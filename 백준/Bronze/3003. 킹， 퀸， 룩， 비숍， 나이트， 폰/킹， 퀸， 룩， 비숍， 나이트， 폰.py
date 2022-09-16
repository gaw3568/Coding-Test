white_chess = [1,1,2,2,2,8]

user_having = list(map(int, input().split()))

for i in range(6):
    print(white_chess[i] - user_having[i], end=' ')