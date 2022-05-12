# 경로 압축(Path Compression)을 이용한 서로소 집합 알고리즘
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i # parent 테이블 -> 루트 노드를 자기 자신으로 초기화

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()
# 부모 테이블
for i in range(1, v+1):
    print(parent[i], end = " ")

"""
input:
6 4
1 4
2 3
2 4
5 6
output:
1 1 1 1 5 5 
1 1 1 1 5 5
"""