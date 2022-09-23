def solution(phone_number):
    answer = list(phone_number)

    for i in range(0, len(answer)-4):
        answer[i] = "*"
        
    return "".join(answer)