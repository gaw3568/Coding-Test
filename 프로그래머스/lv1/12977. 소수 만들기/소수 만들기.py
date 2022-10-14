from itertools import combinations
def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        item = sum(i)
        if len([x for x in range(1, (item // 2) + 1) if item % x == 0]) == 1:
            answer += 1
    return answer