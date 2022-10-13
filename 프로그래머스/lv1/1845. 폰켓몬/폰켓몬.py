from itertools import combinations
def solution(nums):
    max_kind = 0
    length = len(nums) // 2
    nums = set(nums)
    
    for i in nums:
        if max_kind < length:
            max_kind += 1
            
    return max_kind