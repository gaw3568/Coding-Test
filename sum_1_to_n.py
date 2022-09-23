# 1부터 N까지의 합 구하기

from time import time

N = int(input("1부터 N까지 : "))

# 일반적인 방법
sum_1 = 0
start_ = time()
for i in range(1,N+1):
    sum_1 += i
end_ = time()
print(f"총 합 : {sum_1}")
print(f"총 소요시간 : {round(end_ - start_)}")

# 가우스 덧셈 이용하는 방법
start_2nd = time()
sum_2 = (N * (N + 1)) // 2
end_2nd = time()
print(f"총 합 : {sum_2}")
print(f"총 소요시간 : {end_2nd - start_2nd}")
