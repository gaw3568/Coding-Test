def solution(s):
    p_sum = s.lower().count("p")
    y_sum = s.lower().count("y")
    if p_sum == y_sum:
        return True
    else:
        return False