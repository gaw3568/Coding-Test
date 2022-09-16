# 큰 수의 법칙 (그리디 문제)
"""
N : N개의 자연수
M : 숫자가 더해지는 횟수
K : K번 초과되지 않는 수
"""
import time
n, m, k = map(int, input().split())

list_number = list(map(int, input().split()))


list_number.sort()
first_num = list_number[n-1]
second_num = list_number[n-2]

result = 0

# 걸리는 시간 측정
start_time = time.time()

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_num
        m -= 1
    if m == 0:
        break
    result += second_num
    m -= 1

end_time = time.time()
print(result)

print(format(end_time - start_time, ".5f"))