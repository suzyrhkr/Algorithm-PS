import sys, copy
from collections import deque

input = sys.stdin.readline
r ,c, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(r)]
w = int(input())
wall_info = [list(map(int, input().split())) for _ in range(w)]

dx = [0, 0, -1, 1] # 오른쪽, 왼쪽, 위, 아래
dy = [1, -1, 0, 0]

space = [[0]*c for _ in range(r)]
search_list = [] # 조사해야 하는 칸
ac_list = [] # 온풍기 칸
for i in range(r):
    for j in range(c):
        if info[i][j] == 5:
            search_list.append((i,j))
        elif 1 <= info[i][j] and info[i][j] <= 4:
            ac_list.append((i, j, info[i][j]))

# wall_info 처리
wall = []
for x, y, t in wall_info:
    if t == 0:
        wall.append([((x - 1) - 1, (y - 1)), ((x - 1), (y - 1))])
        wall.append([((x - 1), (y - 1)), ((x - 1) - 1, (y - 1))])
    elif t == 1:
        wall.append([((x - 1), (y - 1)), ((x - 1), (y - 1) + 1)])
        wall.append([((x - 1), (y - 1) + 1), ((x - 1), (y - 1))])

def ac():
    for i, j, direction in ac_list:
        if direction == 1:
            x_list, y_list = [-1, 0, 1], [1, 1, 1]
        elif direction == 2:
            x_list, y_list = [-1, 0, 1], [-1, -1, -1]
        elif direction == 3:
            x_list, y_list = [-1, -1, -1], [-1, 0, 1]
        elif direction == 4:
            x_list, y_list = [1, 1, 1], [-1, 0, 1]
        # bfs
        visited = [[False]*c for _ in range(r)]
        i, j = i + dx[direction-1], j + dy[direction-1]
        queue = deque([([i, j, 5])])
        visited[i][j] = True
        space[i][j] += 5
        while queue:
            x, y, level = queue.popleft()
            if level == 0:
                break
            for idx in range(3):
                nx, ny = x + x_list[idx], y + y_list[idx]
                if (0 <= nx and nx < r and 0 <= ny and ny < c) and not visited[nx][ny]:
                    if 1 < level:
                        if abs(x-nx) + abs(y-ny) == 1: 
                            if [(x,y), (nx, ny)] not in wall:
                                queue.append((nx, ny, level - 1))
                                visited[nx][ny] = True
                                space[nx][ny] += level - 1
                        else: 
                            if (x,ny) == (x+dx[direction-1], y+dy[direction-1]):
                                mid_x, mid_y = nx, y
                            else:
                                mid_x, mid_y = x, ny
                            if [(x,y), (mid_x, mid_y)] not in wall and [(mid_x, mid_y), (nx,ny)] not in wall:
                                queue.append((nx, ny, level - 1))
                                visited[nx][ny] = True
                                space[nx][ny] += level - 1


def change_temperature():
    new_space = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if 4 <= space[i][j]:
                for idx in range(4):
                    nx, ny = i + dx[idx], j + dy[idx]
                    if (0 <= nx and nx < r and 0 <= ny and ny < c) and space[nx][ny] < space[i][j]:
                        if [(i,j), (nx,ny)] in wall:
                            continue
                        diff = (space[i][j] - space[nx][ny]) // 4
                        new_space[nx][ny] += diff
                        new_space[i][j] -= diff
    for i in range(r):
        for j in range(c):
            space[i][j] += new_space[i][j]

def outside():
    for i in range(r):
        for j in range(c):
            if i in [0, r-1] or j in [0, c-1]:
                if 0 < space[i][j]:
                    space[i][j] -= 1

chocolate = 0
while True:
    # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴 
    ac()
    # 2. 온도 조절
    change_temperature()
    # 3. 온도가 1 이상인 가장 바깥쪽 칸 -1
    outside()
    # 4. 초콜릿 + 1
    chocolate += 1
    # 온도를 조사해야 하는 칸의 온도 K 이상인지 검사
    flag = True
    for i, j in search_list:
        if space[i][j] < k:
            flag = False
            break
    if flag or 100 < chocolate: 
        break

print(chocolate)

#---other solution(wall 정보: 리스트 순회가 아닌 2차원 리스트 값 확인 방법으로 수정)---
import sys, copy
from collections import deque

input = sys.stdin.readline
r ,c, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(r)]
w = int(input())
wall_info = [list(map(int, input().split())) for _ in range(w)]

dx = [0, 0, -1, 1] # 오른쪽, 왼쪽, 위, 아래 (온풍기의 방향)
dy = [1, -1, 0, 0]

space = [[0]*c for _ in range(r)]
search_list = [] # 조사해야 하는 칸
ac_list = [] # 온풍기 칸
for i in range(r):
    for j in range(c):
        if info[i][j] == 5:
            search_list.append((i,j))
        elif 1 <= info[i][j] and info[i][j] <= 4:
            ac_list.append((i, j, info[i][j]-1))

# 바람 부는 방향 정의 (온풍기 방향과는 순서가 다름)
wx = [0, 1, 0, -1] # 우 하 좌 상
wy = [1, 0, -1, 0]
wall = [[[False]*4 for _ in range(c)] for _ in range(r)]
for x, y, t in wall_info:
    x, y = x-1, y-1
    if t == 0:
        wall[x][y][3] = True
        wall[x-1][y][1] = True
    elif t == 1:
        wall[x][y][0] = True
        wall[x][y+1][2] = True

def ac():
    for i, j, direction in ac_list:
        if direction == 0: # 오른쪽
            x_list, y_list = [-1, 0, 1], [1, 1, 1]
        elif direction == 1: # 왼쪽
            x_list, y_list = [1, 0, -1], [-1, -1, -1]
        elif direction == 2: # 위쪽
            x_list, y_list = [-1, -1, -1], [-1, 0, 1]
        elif direction == 3: # 아래쪽
            x_list, y_list = [1, 1, 1], [1, 0, -1]
        # bfs
        visited = [[False]*c for _ in range(r)]
        i, j = i + dx[direction], j + dy[direction] # 온풍기 방향으로 한 칸 이동
        queue = deque([([i, j, 5])])
        visited[i][j] = True
        space[i][j] += 5

        for d in range(4):
            if (dx[direction], dy[direction]) == (wx[d], wy[d]):
                num = d # 바람 부는 방향 체크
                break

        while queue:
            x, y, level = queue.popleft()
            for idx in range(3):
                nx, ny = x + x_list[idx], y + y_list[idx] 
                # 방문하지 않은 경우
                if (0 <= nx and nx < r and 0 <= ny and ny < c) and not visited[nx][ny]:
                    if 1 < level: 
                        if wall[nx][ny][(num+2) % 4]: # 벽 있는 경우
                            continue

                        if idx == 0:
                            if wall[x][y][(num-1) % 4]:
                                continue
                        elif idx == 2:
                            if wall[x][y][(num+1) % 4]:
                                continue

                        queue.append((nx, ny, level - 1))
                        visited[nx][ny] = True
                        space[nx][ny] += level - 1
                    if level == 0:
                        break

def change_temperature():
    new_space = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if 4 <= space[i][j]:
                for idx in range(4):
                    nx, ny = i + wx[idx], j + wy[idx]
                    if (0 <= nx and nx < r and 0 <= ny and ny < c) and space[nx][ny] < space[i][j]:
                        if wall[i][j][idx]:
                            continue
                        diff = (space[i][j] - space[nx][ny]) // 4
                        new_space[nx][ny] += diff
                        new_space[i][j] -= diff
    for i in range(r):
        for j in range(c):
            space[i][j] += new_space[i][j]

def outside():
    for i in range(r):
        for j in (0, c-1):
            if space[i][j]:
                space[i][j] -= 1
    for i in (0, r-1):
        for j in range(1, c-1):
            if space[i][j]:
                space[i][j] -= 1

chocolate = 0
while True:
    # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴 / rotation
    ac()
    # 2. 온도 조절
    change_temperature()
    # 3. 온도가 1 이상인 가장 바깥쪽 칸 -1
    outside()
    # 4. 초콜릿 + 1
    chocolate += 1
    # 온도를 조사해야 하는 칸의 온도 K 이상인지 검사 -> break
    flag = False
    for i, j in search_list:
        if space[i][j] < k:
            flag = True 
            break

    if not flag: 
        break
    if 100 < chocolate: 
        break

print(chocolate)

