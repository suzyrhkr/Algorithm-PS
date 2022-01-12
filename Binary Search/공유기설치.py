n,c = list(map(int, input().split()))
home = [int(input()) for _ in range(n)]

home.sort()

start, end = home[1]-home[0], home[-1]-home[0]
answer = 0

while start<=end:

    mid = (start+end)//2
    first_home = home[0]
    cnt = 1

    for i in range(1,n):
        if first_home+mid <= home[i]:
            first_home = home[i]
            cnt += 1

    if c<=cnt:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)
