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