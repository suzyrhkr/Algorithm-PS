'''시간 초과'''
import sys
sys.stdin = open('./input.txt', 'r')
n, m = map(int, sys.stdin.readline().strip().split())
space = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    space_line = []
    for j in range(n):
        space_line.append([line[j],False]) # 물의 양/구름 여부
    space.append(space_line)
ds = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 대각선 index 1, 3, 5, 7

def move(d, s):
    cloud_position = []
    for i in range(n):
        for j in range(n):
            # 현재 구름이 있는 경우, 자리 이동
            if space[i][j][1] == True: 
                space[i][j][1] = False
                nx = i + s * dx[d-1]
                ny = j + s * dy[d-1]
                # exception 처리
                if nx < 0: 
                    while nx < 0:
                        nx += n
                if ny < 0: 
                    while ny < 0:
                        ny += n
                if n <= nx:
                    while n <= nx:
                        nx -= n
                if n <= ny:
                    while n <= ny:
                        ny -= n
                space[nx][ny][0] += 1
                cloud_position.append([nx,ny])
    return cloud_position

def copy_magic(cloud_position):
    for x, y in cloud_position:
        cnt = 0
        for j in range(1,8,2):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if 0 < space[nx][ny][0]:
                    cnt += 1
        space[x][y][0] += cnt
    return

def water_amount_two(cloud_position):
    for i in range(n):
        for j in range(n):
            if 2 <= space[i][j][0] and [i,j] not in cloud_position:
                space[i][j][1] = True
                space[i][j][0] -= 2
    return 

def magic(d, s):
    # d 방향, s칸 이동, 구름 자리 물의 양 1 증가
    cloud_position = move(d, s)
    # 물이 증가한 칸, 물복사버그 마법
    copy_magic(cloud_position)
    # 바구니 저장된 물의 양 2인 칸에 구름 생성, 물의 양 2 감소 (조건: 구름 자리 뺀 곳만)
    water_amount_two(cloud_position)
    return

# 바구니 물의 양 합 출력 func
def total_amount():
    result = 0
    for i in range(n):
        for j in range(n):
            result += space[i][j][0]
    return result

# 초기 구름 위치
space[n-2][0][1], space[n-2][1][1] = True, True
space[n-1][0][1], space[n-1][1][1] = True, True

# main
for d, s in ds:
    magic(d, s)

print(total_amount())

#---other solution(deque)---
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
space = []
for i in range(n):
    line = list(map(int, input().split()))
    space_line = []
    for j in range(n):
        space_line.append([line[j],False]) # 물의 양/구름 여부
    space.append(space_line)
ds = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 대각선 index 1, 3, 5, 7

clouds = [[n-2,0], [n-2,1], [n-1,0], [n-1,1]]
clouds = deque(clouds)

def move_cloud(d, s):
    current_length = len(clouds)
    for _ in range(current_length):
        x, y = clouds.popleft()
        nx = (x + s * dx[d-1]) % n
        ny = (y + s * dy[d-1]) % n
        clouds.append([nx, ny])
        space[nx][ny][0] += 1
        space[nx][ny][1] = True # 구름이 사라진 자리 표시

def copy_magic():
    while clouds:
        x, y = clouds.popleft()
        cnt = 0
        for j in range(1,8,2):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if 0 < space[nx][ny][0]:
                    cnt += 1
        space[x][y][0] += cnt

def make_cloud():
    for i in range(n):
        for j in range(n):
            if 2 <= space[i][j][0] and space[i][j][1] == False:
                clouds.append([i,j])
                space[i][j][0] -= 2
            # 구름 여부 초기화
            space[i][j][1] = False
    return 

def total_amount():
    result = 0
    for i in range(n):
        for j in range(n):
            result += space[i][j][0]
    return result

# main
for d, s in ds:
    # d 방향, s칸 이동, 구름 자리 물의 양 1 증가
    move_cloud(d, s)
    # 물이 증가한 칸, 물 복사 버그 마법
    copy_magic()
    # 바구니 저장된 물의 양 2인 칸에 구름 생성, 물의 양 2 감소 (조건: 구름 자리 뺀 곳만)
    make_cloud()

print(total_amount())