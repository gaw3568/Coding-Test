def solution(n, m):
    if n < m:   n, m = m, n
    a = n
    b = m
    
    while (a % b) != 0:
        tmp_num = a % b
        a = b
        b = tmp_num
    return [b, int(n * m) / b]