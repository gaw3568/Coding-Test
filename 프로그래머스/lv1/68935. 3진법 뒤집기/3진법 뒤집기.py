def solution(n):
    ch_str = ""
    while n > 0:
        n, mod = divmod(n, 3)
        ch_str += str(mod)
    return int(ch_str, 3)
