import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
space = []
houses, chicken = [], []

for i in range(n): 
    info = list(map(int, input().split()))
    for j, x in enumerate(info):
        if info[j] == 1:
            houses.append((i,j))
        elif info[j] == 2:
            chicken.append((i,j))

candidates = list(combinations(chicken, m))

def calculate_distance(a, b): # 거리 계산
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_sum(candidate):
    result = 0
    for h in houses:
        ret = float('inf')
        for ch in candidate:
            ret = min(ret, calculate_distance(h, ch))
        result += ret
    return result

answer = float('inf')
for c in candidates:
    answer = min(answer, get_sum(c))

print(answer)

