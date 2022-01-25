n = int(input())
t, p = [], []
max_val = 0

dp = [0]*(n+1)

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time = i+t[i]
    if time<=n:
        dp[i] = max(p[i]+dp[time], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)


