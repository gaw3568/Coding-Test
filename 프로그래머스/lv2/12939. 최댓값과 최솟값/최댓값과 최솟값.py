def solution(s):
    new_s = list(map(int, s.split(" ")))
    answer = f"{min(new_s)} {max(new_s)}"
    return answer