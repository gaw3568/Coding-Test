# 벌집의 총 개수
N = int(input())

count = 1

start_honeycom = 1

while N > start_honeycom:
    start_honeycom += (6 * count)
    count += 1
print(count)