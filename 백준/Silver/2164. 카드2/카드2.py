from collections import deque

N = int(input())

card_list = deque([num for num in range(1, N+1)])

while card_list:
    if len(card_list) == 1:
        break
    card_list.popleft()
    pop_item = card_list.popleft()
    card_list.append(pop_item)

print(card_list[0])