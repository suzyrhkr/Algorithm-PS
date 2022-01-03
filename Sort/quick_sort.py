# quick sort code for python 

arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if pivot<x]

    return quick_sort(left) + pivot + quick_sort(right_side)

print(quick_sort(arr))