def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# input
v, e = map(int, input().split())
parent = [0] * (v+1)

# parent 테이블, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() # 간선을 비용순으로 정렬

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는 경우, Union 함수 호출
        union_parent(parent, a, b)
        result += cost

print(result)
