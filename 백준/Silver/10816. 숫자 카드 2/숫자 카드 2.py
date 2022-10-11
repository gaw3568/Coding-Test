import sys

N = sys.stdin.readline()
N_list = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
M_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()

cnt = {}

for i in N_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in M_list:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")