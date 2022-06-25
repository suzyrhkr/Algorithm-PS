from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r, c = len(maps), len(maps[0])
    graph = [[-1 for _ in range(c)] for _ in range(r)]
    graph[0][0] = 1
    queue = deque([[0, 0]])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])

    answer = graph[-1][-1]
    return answer