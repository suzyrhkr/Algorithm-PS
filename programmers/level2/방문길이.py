
def solution(dirs):
    answer = 0
    direction = {}
    direction['U'] = [0, 1]
    direction['D'] = [0, -1]
    direction['L'] = [-1, 0]
    direction['R'] = [1, 0]

    x, y = 0, 0
    visited = set()

    for d in dirs:
        dx, dy = direction[d]
        
        nx, ny = x + dx, y + dy
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
        
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny , x, y))
            answer += 1
        
        x, y = nx, ny
    
    return answer