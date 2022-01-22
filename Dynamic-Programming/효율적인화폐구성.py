n, m = list(map(int, input().split()))
money = [int(input()) for _ in range(n)]

d = [-1]*(m+1)
d[0] = 0

for i in range(n):
    for j in range(money[i],m+1):
        if d[j-money[i]]!=-1:
            d[j] = d[j-money[i]]+1

print(d[m])
