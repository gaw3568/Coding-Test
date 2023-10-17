import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())

_heapq = list()

for _ in range(N):
    num = int(sys.stdin.readline())
    if num:
        heappush(_heapq, (abs(num), num))
    else:
        if not _heapq:
            print(0)
        else:
            pop_num = heappop(_heapq)
            print(pop_num[1])
