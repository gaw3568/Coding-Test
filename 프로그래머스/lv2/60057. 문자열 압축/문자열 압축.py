def solution(s):
    result = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        tmp_str = ""
        count = 1
        cut_i = s[:i]
        
        # range(1, 9, 1)
        for j in range(i, len(s) + i, i):
            if cut_i == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    tmp_str += cut_i
                else:
                    tmp_str += str(count) + cut_i
                cut_i = s[j:j+i]
                count = 1
        
        result.append(len(tmp_str))

    return min(result)