def solution(n):
    fibo_num = [] * 100001
    for i in range(n + 1):
        if i == 0 or i == 1:
            fibo_num.append(i)
        else:
            tmp_num = fibo_num[i-1] + fibo_num[i-2]
            fibo_num.append(tmp_num % 1234567)
    return fibo_num[-1]
        