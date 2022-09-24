def solution(price, money, count):
    total_sum = 0
    for i in range(1, count + 1):
        total_sum += (price * i)
    if total_sum <= money:
        return 0
    else:
        return total_sum - money