def solution(n):
    list_n = [i for i in range(1, (n // 2) + 1) if n % i == 0]
    list_n.append(n)
    list_n.sort()
    return list_n