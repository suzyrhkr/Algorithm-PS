import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
distance = [INF]*(n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        node, dist = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for v, d in graph[node]:
            cost = dist + d
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (v, cost))

dijkstra(c)

max_num, max_length = 0, 0
for i in range(1, n+1):
    if distance[i] != INF:
        max_num += 1
        max_length = max(distance[i], max_length)

print(max_num - 1, max_length)