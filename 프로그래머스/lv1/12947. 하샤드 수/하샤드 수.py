def solution(x):
    heashad_num = sum(list(map(int, str(x)[0:])))
    if x % heashad_num == 0:
        return True
    else:
        return False