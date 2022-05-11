# 한 노드에서 다른 모든 노드로 가는 최단 경로
# Time Complexity: O(Elog(V)) E: # of edge / V: # of node
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드 
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 노드라면 무시
            continue 
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

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