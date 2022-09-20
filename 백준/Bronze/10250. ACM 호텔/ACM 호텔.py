import sys
input = sys.stdin.readline
test_case = int(input())

for i in range(test_case):
    H,W,N = map(int, input().split())

    floor = N % H
    room = (N // H) + 1

    if floor == 0:
        floor = H
        room -= 1

    print(floor * 100 + room)
