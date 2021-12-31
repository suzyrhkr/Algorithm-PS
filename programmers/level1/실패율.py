def solution(N, stages):
    fail_ratio = {}
    len_stages = len(stages)

    for i in range(1, N+1):
        if len_stages != 0:
            fail = stages.count(i)
            fail_ratio[i] = fail/len_stages
            len_stages -= fail
        else:
            fail_ratio[i]=0

    return sorted(fail_ratio, key=lambda x: fail_ratio[x], reverse=True)