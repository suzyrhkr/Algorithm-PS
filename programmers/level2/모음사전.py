def solution(word):
    answer = 0
    chs = ['A', 'E', 'I', 'O', 'U']
    result = set()
    cnt = 0
    
    def backtracking(arr):
        nonlocal answer, cnt, result
        if 5 < len(arr):
            return
            
        arr = "".join(arr)
        if 0 < len(arr) and arr not in result:
            result.add(arr)
            cnt += 1
            if arr == word:
                answer = cnt
                return
        
        arr = list(arr)
        for i in range(5):
            arr.append(chs[i])
            backtracking(arr)
            arr.pop()
    
    backtracking([])
    
    return answer