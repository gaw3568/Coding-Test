def solution(babbling):
    talk_list = ["aya","ye","woo","ma"]
    answer = 0
    for word in babbling:
        for i in talk_list:
            if (i * 2) not in word:
                word = word.replace(i,"")
        if len(word) == 0:
            answer += 1
    return answer