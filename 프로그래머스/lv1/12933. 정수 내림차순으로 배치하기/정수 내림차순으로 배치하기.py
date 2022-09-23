def solution(x):
    num_list = list(map(int, str(x)))
    num_list.sort(reverse=True)
    answer = ""
    for i in num_list:
        answer += str(i)
    return int(answer)

"""
def solution(x):
    answer = list(str(x))
    answer.sort(reverse=True)
    return int("".join(answer))
"""
