#---solution(module bisect)---
import bisect 

n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = bisect.bisect_left(arr, x)
right = bisect.bisect_right(arr, x)

if left==right:
    print(-1)
else:
    print(right-left)


#---other solution(binary search)---
n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = n-1

left, right = 0, 0

while start <= end:
    if start>end:
        break
    
    mid = (start+end)//2

    if (mid==0 or arr[mid-1]<x) and arr[mid]==x:
        left = mid
        break
    elif x <= arr[mid]:
        end = mid-1
    else:
        start = mid+1


start = 0
end = n-1

while start <= end:
    if start>end:
        break
    
    mid = (start+end)//2

    if (mid==n-1 or x<arr[mid+1]) and arr[mid]==x:
        right = mid
        break
    elif x < arr[mid]:
        end = mid-1
    else:
        start = mid+1
    
if left==right:
    print(-1)
else:
    print(right-left+1)