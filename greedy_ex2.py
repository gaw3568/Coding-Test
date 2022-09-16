# 숫자 카드 게임 (그리디 문제)
# N : 행, M :열

import sys
n, m = map(int, sys.stdin.readline().split())

result = 0

for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    min_num = min(data)
    result = max(result, min_num)

print(result)