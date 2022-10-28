def solution(answers):
    first_math = [1, 2, 3, 4, 5]
    second_math = [2, 1, 2, 3, 2, 4, 2, 5]
    third_math = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    
    answer = []
    
    for i in range(len(answers)):
        if first_math[i % len(first_math)] == answers[i]:
            score[0] += 1
        if second_math[i % len(second_math)] == answers[i]:
            score[1] += 1
        if third_math[i % len(third_math)] == answers[i]:
            score[2] += 1
            
    for i, j in enumerate(score):
        if j == max(score):
            answer.append(i+1)
    return answer