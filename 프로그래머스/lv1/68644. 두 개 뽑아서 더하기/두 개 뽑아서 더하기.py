from itertools import combinations
def solution(numbers):
    result = set()
    for i,j in combinations(numbers,2):
        result.add(i + j)
    result = list(result)
    result.sort()
    return result
