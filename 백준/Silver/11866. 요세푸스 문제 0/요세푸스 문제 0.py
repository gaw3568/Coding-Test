from collections import deque

N, K = map(int, input().split())

queue = deque()
result = []

for i in range(1, N+1):
    queue.append(i)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end="")
for num in result:
    if result[-1] == num:
        print(f"{num}>")
    else:
        print(num, end=", ")