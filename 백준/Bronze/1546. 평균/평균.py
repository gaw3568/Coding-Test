N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

for i in range(len(score_list)):
    new_score = (score_list[i] / max_score) * 100
    score_list[i] = new_score

print(sum(score_list)/ N)