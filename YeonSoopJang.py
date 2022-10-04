# 코드 연습장
from collections import deque

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([x+y for x,y in zip(arr1[i],arr2[i])])
    return answer
    
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print([x+y for x,y in zip([1,2,3],[3,4,5])])   
print(solution(arr1=arr1, arr2=arr2))
print("--------------------")

N, K = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

for i in range(K):
    if a_list[i] < b_list[i]:
        a_list[i], b_list[i] = b_list[i], a_list[i]
print(sum(a_list))