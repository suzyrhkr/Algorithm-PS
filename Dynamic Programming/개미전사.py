n = int(input())
food = list(map(int, input().split()))

d = [0]*101

d[0] = food[0]
d[1] = max(food[0], food[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+food[i])

print(d[n-1])