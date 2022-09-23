import math
def solution(n):
    answer = 0
    num = math.sqrt(n)
    if num == int(num):
        answer = (num + 1)**2
    else:
        answer = -1
    return answer