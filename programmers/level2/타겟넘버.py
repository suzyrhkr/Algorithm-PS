# DFS
answer = 0

def dfs(numbers, idx, target, result):
    global answer
    if len(numbers) == idx:
        if target == result:
            answer += 1
        return
    
    dfs(numbers, idx+1, target, result+numbers[idx])
    dfs(numbers, idx+1, target, result-numbers[idx])
    
def solution(numbers, target):
    dfs(numbers, 0, target, 0)
    return answer

# BFS
def solution(numbers, target):
    queue = [0]
    
    for num in numbers:
        child = []
        for parent in queue:
            child.append(parent+num)
            child.append(parent-num)
        queue = child
    
    return queue.count(target)

'''
다른 scope에 있는 변수 사용 문제 reference:
https://juhi.tistory.com/6
'''