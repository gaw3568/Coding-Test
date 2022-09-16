# 1이 될 때까지 (그리디 문제)
n, k = map(int, input().split())

count = 0

# n = 25, k = 3

while True:
    new_n = (n // k) * k
    count += (n - new_n)
    n = new_n
    
    if n < k:
        break    
    count += 1
    n = n // k

count += (n - 1)

print(count)