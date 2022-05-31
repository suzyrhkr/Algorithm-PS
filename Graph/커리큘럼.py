from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1) # 진입차수 테이블
graph = [[] for i in range(n+1)]
cost = [0] * (n+1) 

for i in range(1, n+1):
    info = list(map(int, input().split()))
    cost[i] = info[0]

    for x in info[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(cost)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + cost[i])
            indegree[i] -= 1
            if indegree == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()

