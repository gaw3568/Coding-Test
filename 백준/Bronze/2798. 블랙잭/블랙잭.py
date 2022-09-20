N,M = map(int, input().split())
N_card_list = list(map(int, input().split()))
result = 0

for i in range(N):
    three_pick_cards = 0
    # N_card_list[i]
    for j in range(i + 1, N):
        # N_card_list[j]
        for k in range(j + 1, N):
            # N_card_list[k]
            three_cards = N_card_list[i] + N_card_list[j] + N_card_list[k]
            if three_cards > M:
                continue
            else:
                result = max(result, three_cards)
print(result)

