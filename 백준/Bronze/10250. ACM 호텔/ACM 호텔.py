test_case = int(input())

for i in range(test_case):
    H,W,N = map(int, input().split())

    floor = 0
    room = 0

    if N % H == 0:
        floor = H * 100
        room = N // H
    else:
        floor = (N % H) * 100
        room = (N // H) + 1
    print(floor + room)
