import sys
from collections import deque

input = sys.stdin.readline
n, m, gas = map(int, input().split()) # n*n / 승객 m명 / 초기 gas 양
space = [list(map(int, input().split())) for _ in range(n)]
driver_x, driver_y = map(int, input().split()) # 1 <= x <= n
driver_x, driver_y = driver_x - 1, driver_y - 1
path = []
for i in range(m):
    start_x, start_y, end_x, end_y = list(map(int, input().split()))
    path.append([start_x - 1, start_y - 1, end_x - 1, end_y - 1])

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(start_x, start_y):
    new_space = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    queue = [start_x, start_y]
    queue = deque([queue])
    visited[start_x][start_y] = True
    pos = []
    while queue:
        x, y = queue.popleft()
        for p in path: # 승객 있는지 체크
            if (x, y) == (p[0], p[1]):
                pos.append([x, y, new_space[x][y]])
                break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx and nx < n and 0 <= ny and ny < n):
                if space[nx][ny] != 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    new_space[nx][ny] = new_space[x][y] + 1
    return pos

def bfs2(start_x, start_y):
    new_space = [[None]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    new_space[start_x][start_y] = 0
    queue = [start_x, start_y]
    queue = deque([queue])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx and nx < n and 0 <= ny and ny < n):
                if space[nx][ny] != 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    new_space[nx][ny] = new_space[x][y] + 1
    return new_space

flag = False
while True:
    passengers = bfs(driver_x, driver_y)
    if path and not passengers: # 모든 손님을 이동시킬 수 없는 경우
        flag = True
        break

    passengers.sort(key=lambda x: (x[2], x[0], x[1]))
    shortest_path = passengers[0][-1]
    src_x, src_y = passengers[0][0], passengers[0][1]

    # 승객을 데리러 감
    if gas < shortest_path:
        flag = True
        break
    gas -= shortest_path
    driver_x, driver_y = src_x, src_y

    # 승객을 목적지에 데려다 줌
    for p in path: # 승객의 목적지 찾기
        if (src_x, src_y) == (p[0], p[1]):
            des_x, des_y = p[2], p[3]

    path_info = bfs2(driver_x, driver_y)
    shortest_path = path_info[des_x][des_y]
    if shortest_path == None:
        flag = True
        break
    if gas < shortest_path:
        flag = True
        break
    gas -= shortest_path
    driver_x, driver_y = des_x, des_y

    # 연료 충전
    gas += 2 * shortest_path

    for p in path[:]:
        if [src_x, src_y] == [p[0], p[1]]:
            path.remove(p)
    if not path:
        break

if flag:
    print(-1)
else:
    print(gas)