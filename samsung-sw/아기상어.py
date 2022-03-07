from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

shark_r, shark_c = 0, 0
shark_weight = 2

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_r, shark_c = i, j
            space[shark_r][shark_c] = 0
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# calculate shortest distance
def bfs():
    distance = [[-1]*n for _ in range(n)]
    queue = deque([(shark_r, shark_c)])
    distance[shark_r][shark_c] = 0

    while queue:
        q_x, q_y = queue.popleft()
        for x, y in zip(dx, dy):
            nx, ny = q_x + x, q_y + y
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # pass
                if distance[nx][ny]==-1 and space[nx][ny] <= shark_weight:
                    distance[nx][ny] = distance[q_x][q_y] + 1
                    queue.append((nx,ny))
    return distance

# calculate (x,y) and min distance
def find(distance):
    x, y = 0, 0
    min_distance = float('inf')

    for i in range(n):
        for j in range(n):
            if distance[i][j]!=-1 and 1 <= space[i][j] and space[i][j] < shark_weight:
                if distance[i][j] < min_distance:
                    x, y = i, j
                    min_distance = distance[i][j]
    
    if min_distance==float('inf'):
        return None
    else:
        return x, y, min_distance

result = 0
ate = 0

while True:
    ret = find(bfs())
    if ret == None:
        print(result)
        break
    else:
        shark_r, shark_c = ret[0], ret[1]
        result += ret[2]
        space[shark_r][shark_c] = 0
        ate += 1

        if shark_weight <= ate:
            shark_weight += 1
            ate = 0