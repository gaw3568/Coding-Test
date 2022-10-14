from itertools import combinations
def solution(number):
    answer = 0
    for (a,b,c) in combinations(number, 3):
        if (a + b + c) == 0:
            answer += 1
    return answer