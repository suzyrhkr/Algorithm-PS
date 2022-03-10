def bfs(wires, visited, start, n):
    queue = [start]
    cnt = 1
    
    while queue:
        node = queue.pop(0)
        for i in range(len(wires)):
            if wires[i][0] == node:
                if not visited[wires[i][1]]:
                    visited[wires[i][1]] = True
                    queue.append(wires[i][1])
                    cnt += 1
            elif wires[i][1] == node:
                if not visited[wires[i][0]]:
                    visited[wires[i][0]] = True
                    queue.append(wires[i][0])
                    cnt += 1
                    
    diff = abs((n-cnt) - cnt)
    return diff
    
def solution(n, wires):
    min_abs = float('inf')
    
    for i in range(len(wires)):
        visited = [False]*101
        visited[wires[i][0]] = True
        visited[wires[i][1]] = True

        diff = bfs(wires, visited, wires[i][0], n)
        min_abs = min(min_abs, diff)

    return min_abs