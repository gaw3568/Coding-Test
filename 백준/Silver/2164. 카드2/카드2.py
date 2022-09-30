from collections import deque
N = int(input())
new_list = deque([x for x in range(1, N + 1)])

while True:
    if len(new_list) == 1:
        print(new_list[0])
        break
    new_list.popleft()
    new_list.append(new_list.popleft())