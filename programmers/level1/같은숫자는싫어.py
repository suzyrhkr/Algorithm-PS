def solution(arr):
    answer = []
    set_arr = list(set(arr))
    arr = "".join(map(str, arr))
    
    for ch in set_arr:
        while str(ch)*2 in arr:
            arr = arr.replace(str(ch)*2, str(ch))
        
    return list(map(int, arr))

#---other solution---

def solution(arr):
    answer = []
    stack = []

    for n in arr:
        if not stack or stack[-1]!=n:
            stack.append(n)
      
    return stack