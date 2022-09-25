def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        a = A[i]
        b = B[i]
        answer += (a * b)
    return answer