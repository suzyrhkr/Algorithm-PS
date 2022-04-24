import sys

input = sys.stdin.readline
n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
max_val = 0

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if n < i + info[i][0]:
        dp[i] = max_val
        continue
    dp[i] = max(info[i][1] + dp[i + info[i][0]], max_val)
    max_val = dp[i]
    
print(dp[0])
