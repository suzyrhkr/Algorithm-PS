def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            prior_max = 0
            for k in range(4):
                if j != k:
                    prior_max = max(land[i-1][k], prior_max)
            land[i][j] += prior_max
            
    return max(land[-1])