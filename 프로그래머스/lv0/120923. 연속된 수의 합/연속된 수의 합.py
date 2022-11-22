def solution(num, total):
    sum = 0
    for i in range(num):
        sum += i
    total -= sum
    basic_num = total / num
    answer = [i + basic_num for i in range(num)]
    return answer