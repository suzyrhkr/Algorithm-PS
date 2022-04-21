import sys, copy
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)] 
dice = [[0,2,0], [4,1,3], [0,5,0], [0,6,0]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
curr_x, curr_y = 0, 0

def move_dice(direction):
    # 0:동 / 1:남 / 2:서 / 3:북
    if direction == 0:
        a, b, c, d = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = d, a, b, c
    elif direction == 1:
        a, b, c, d = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = d, a, b, c
    elif direction == 2:
        a, b, c, d = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = b, c, d, a
    elif direction == 3:
        a, b, c, d = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = b, c, d, a

def bfs(curr_x, curr_y, b):
    c = 1
    queue = deque([(curr_x, curr_y)])
    visited = [[False]*m for _ in range(n)]
    visited[curr_x][curr_y] = True
    # 맨 처음 좌표
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if (0 <= nx and nx < n and 0 <= ny and ny < m):
                if space[nx][ny] == b and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    c += 1
    return c

def move():
    global score, curr_x, curr_y, direction
    nx, ny = curr_x + dx[direction], curr_y + dy[direction] # 주사위 위치 이동
    if not (0 <= nx and nx < n and 0 <= ny and ny < m): # 만약 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 칸 이동
        direction = (direction+2) % 4
        curr_x, curr_y = curr_x + dx[direction], curr_y + dy[direction]
        move_dice(direction)
    else:
        curr_x, curr_y = nx, ny
        move_dice(direction) 

    # 점수 획득
    b = space[curr_x][curr_y]
    # bfs
    c = bfs(curr_x, curr_y, b)
    score += b * c

    # 주사위 이동 방향 결정
    a = dice[3][1]
    if a > b:
        direction = (direction+1) % 4
    elif a < b:
        direction = (direction-1) % 4
    else:
        pass

score = 0
for _ in range(k):
    move()
print(score)

"""
이동: 맨 처음 동쪽으로 이동.
1. 이동 방향으로 한 칸. 칸이 없다면 반대방향으로 한 칸.
2. 도착한 칸에 대한 점수 획득
3. 주사위 아랫면 정수 A / 주사위 칸 정수 B 로 이동 방향 결정

점수 구하는 법:
동서남북으로 연속해서 이동할 수 있는 칸의 수를 구한다.
B * C
"""