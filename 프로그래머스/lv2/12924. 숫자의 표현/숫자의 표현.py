def solution(n):
    answer = []
    for x in range(1, n+1, 2):
        if n % x == 0:
            answer.append(x)
    return len(answer)