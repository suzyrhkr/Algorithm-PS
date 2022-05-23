# Time Complexity: O(V+E)
# 위상 정렬: 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 알고리즘
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1) # 진입차수 테이블
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 처음, 진입차우 0인 노드 모두 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 노드와 연결된 노드에 연결된 간선 제거 -> 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()