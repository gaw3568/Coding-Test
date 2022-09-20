import sys
input = sys.stdin.readline

T_case = int(input())

for case in range(T_case):
    # k층
    k = int(input().rstrip())
    # n호
    n = int(input().rstrip())
    # 0층에 사는 가구원
    k_floor = [x for x in range(1, n+1)]
    
    for i in range(k):
        new_list = []
        for j in range(n):
            new_list.append(sum(k_floor[:j+1]))
        k_floor = new_list
        # 다른 방법
        # k_floor = new_list.copy()
    print(k_floor[-1])