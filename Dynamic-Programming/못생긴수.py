n = int(input())

dp = [0]*n
dp[0] = 1

idx_2, idx_3, idx_5 = 0, 0, 0
next_2, next_3, next_5 = 2, 3, 5

for i in range(1,n):
    dp[i] = min(next_2, next_3, next_5)

    if dp[i] == next_2:
        idx_2 += 1
        next_2 = dp[idx_2]*2

    if dp[i] == next_3:
        idx_3 += 1
        next_3 = dp[idx_3]*3

    if dp[i] == next_5:
        idx_5 += 1
        next_5 = dp[idx_5]*5

print(dp[-1])
