def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer

"""
<다른 방법>
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
"""
