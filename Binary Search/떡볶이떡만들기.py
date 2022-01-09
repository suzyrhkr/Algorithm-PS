n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0 
end = max(rice_cake)

answer = 0

while(start<=end):
    total = 0
    mid = (start+end)//2

    sliced = []
    for x in rice_cake:
        if mid<x:
            total += x-mid

    if total < m:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)

    
