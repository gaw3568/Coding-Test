T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    cycle_a = a % 10

    if cycle_a == 0:
        print(10)
    elif cycle_a in [1,5,6]:
        print(cycle_a)
    elif cycle_a in [4,9]:
        # 지수가 반복되는 횟수 : 2
        cycle_b = b % 2
        if cycle_b == 0:
            print((cycle_a * cycle_a) % 10)
        else:
            print(cycle_a)
    else:
        # 지수가 반복되는 횟수 : 4
        cycle_b = b % 4
        if cycle_b == 0:
            print((cycle_a**4) % 10)
        else:
            print((cycle_a**cycle_b) % 10)