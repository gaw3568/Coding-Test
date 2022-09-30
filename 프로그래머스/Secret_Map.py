# 프로그래머스 카카오 블라인드 코딩 테스트 문제
# 비밀지도 

def secret_map(n, arr1, arr2):
    answer = []
    for i in range(n):
        new_num = bin((arr1[i] | arr2[i]))[2:]
        """
        rjust() 함수 사용해서 공백의 수, 공백을 메워줄 문자를 채워줄 수 있음.
        new_num = new_num.rjust(n, "0")
        """
        if len(new_num) != n:
            new_num = "0" * (n - len(new_num)) + new_num
        new_num = new_num.replace("1","#")
        new_num = new_num.replace("0"," ")
        answer.append(new_num)
    return answer

print(secret_map(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))