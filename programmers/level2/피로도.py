from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n_dungeons = len(dungeons)
    range_list = list(range(n_dungeons))
    ps = list(permutations(range_list, n_dungeons))
    
    for i, p in enumerate(ps):
        curr_k = k
        cnt = 0
        for j in p:
            if curr_k < dungeons[j][0]:
                continue
            curr_k -= dungeons[j][1]
            cnt += 1
        answer = max(answer, cnt)
   
    return answer

#---other solution---
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
