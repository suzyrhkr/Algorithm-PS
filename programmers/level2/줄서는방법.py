#---부분 시간 초과 코드---
def solution(n, k):
    answer = []
    cnt = 0
    nums = list(range(1, n+1))
    visited = [False]*(n+1)
    
    def backtracking(arr):
        nonlocal cnt, answer
        if len(arr) == n:
            cnt += 1
            if cnt == k:
                answer = arr.copy()
            return
        
        for i, p in enumerate(nums):    
            if not visited[p]:
                arr.append(p)
                visited[p] = True
                backtracking(arr)        
                arr.pop()   
                visited[p] = False
        
    backtracking([])

    return answer