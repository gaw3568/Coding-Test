def solution(s):
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if arr == []:
                return False
            else:
                arr.pop()
    return len(arr) == 0

"""
<다른방법>
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        if w == '(':
            x = x + 1
        elif w == ')':
            x = x - 1 
    return x == 0
"""
