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