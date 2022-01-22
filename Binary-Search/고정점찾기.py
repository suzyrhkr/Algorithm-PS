n = int(input())
a = list(map(int, input().split()))

start, end = 0, n-1

answer = None

while start<=end:
    if start>end:
        break
    mid = (start+end)//2

    if a[mid] == mid:
        answer = mid
        break
    elif mid < a[mid]:
        end = mid-1
    else:
        start = mid+1

if not answer:
    print(-1)
else:
    print(answer)