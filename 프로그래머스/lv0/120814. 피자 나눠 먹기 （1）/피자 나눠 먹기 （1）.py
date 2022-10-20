def solution(n):
    pizza = n // 7
    if n % 7 > 0:
        pizza += 1
    return pizza