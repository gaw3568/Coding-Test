def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    answer = len(d)
    return answer