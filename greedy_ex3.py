# 1이 될 때까지 (그리디 문제)
import sys
n, k = map(int, sys.stdin.readline().split())

count = 0

# n = 25, k = 3

while True:
    new_n = (n // k) * k
    count += (n - new_n)
    n = new_n
    
    if n < k:
        break
    
print(count)