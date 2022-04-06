from itertools import combinations

n = int(input())
players = list(range(1, n+1))
capabilities = [list(map(int, input().split())) for _ in range(n)]
info = {}
combination = combinations(players, n//2)

for c in list(combination):
    subset = combinations(c, 2)
    subset_sum = 0
    for s in subset:
        subset_sum += capabilities[s[0]-1][s[1]-1] + capabilities[s[1]-1][s[0]-1]
    info[c] = subset_sum

min_value = float('inf')

for i in info:
    a, b = set(i), set(players)
    sub = list(b-a)
    sub = tuple(sorted(sub))
    min_value = min(min_value, abs(info[i] - info[sub]))

print(min_value)

#---other solution(DFS(back tracking))---
def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)