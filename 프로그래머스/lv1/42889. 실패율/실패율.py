def solution(N, stages):
    total_user = len(stages)
    result = {}
    
    for stage in range(1, N+1):
        if total_user == 0:
            result[stage] = 0
        else:
            fail_count = stages.count(stage)
            result[stage] = fail_count / total_user
            total_user -= fail_count
    
    return sorted(result, key=lambda x: result[x], reverse=True)