# 모든 노드에서 모든 노드로 가는 최단 경로
INF = int(1e9)

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

graph = [[INF]*(n+1) for _ in range(n+1)] # 2차원 리스트, 무한대로 초기화

# 같은 노드에서 같은 노드로 가는 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선 정보를 입력받아서 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c # a -> b / cost: c

# 플로이드 워셜 알고리즘 (점화식)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("X", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

"""
input:
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4 
4 3 2

output:
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
"""