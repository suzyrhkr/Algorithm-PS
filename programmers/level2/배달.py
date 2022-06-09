import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    distance = [float('inf')] * (N+1)

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    q = []
    heapq.heappush(q, (0, 1)) # 시작 노드 
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 노드라면 무시
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  
        
    return len([i for i in distance if i <=K])