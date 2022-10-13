import sys
N = int(sys.stdin.readline())
n_list = []

for _ in range(N):
    n_list.append(list(map(int, sys.stdin.readline().split())))
n_list.sort(key=lambda x:(x[0],x[1]))

for i in n_list:
    print(i[0],i[1])