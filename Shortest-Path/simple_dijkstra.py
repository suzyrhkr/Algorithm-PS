# Time Complexity: O(V^2) V: # of node
import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split()) # 노드 개수 / 간선 개수
start = int(input()) # 시작 노드
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1) # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b / cost: c
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드 선택
def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for end, cost in graph[start]:
        distance[end] = cost

    # 시작 노드를 제외한 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for end, cost in graph[now]:
            now_cost = distance[now] + cost
            if now_cost < distance[end]:
                distance[end] = now_cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("node({}) can not be reached".format(i))
    else:
        print("node({}) distance: {}".format(i, distance[i]))

"""
input:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

output:
node(1) distance: 0
node(2) distance: 2
node(3) distance: 3
node(4) distance: 1
node(5) distance: 2
node(6) distance: 4
"""