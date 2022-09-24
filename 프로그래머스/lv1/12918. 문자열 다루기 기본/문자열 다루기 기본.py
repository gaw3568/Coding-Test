def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if not('0' <= i <= '9'):
                return False
        return True
    else:
        return False