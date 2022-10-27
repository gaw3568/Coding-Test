score = input()

is_even = len(score)

divide_half = (is_even // 2)
left_score = sum(list(map(int, list(score[0:divide_half]))))
right_score = sum(list(map(int, list(score[divide_half:]))))

if left_score == right_score:
    print("LUCKY")
else:
    print("READY")
