def solution(num_list):
    # 홀수
    odd_num = len([x for x in num_list if x % 2 == 1])
    # 짝수
    even_num = len([x for x in num_list if x % 2 == 0])
    
    return [even_num, odd_num]