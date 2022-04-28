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

#---other solution---
# sort 함수 key = lambda를 이용하여 한 번에 정렬한 풀이
# 1' 00

import sys

input = sys.stdin.readline
n = int(input())
info = [list(map(int, input().split())) for _ in range(n*n)]
space = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def calculate_score():
    score = 0
    for i in range(n):
        for j in range(n):
            for k in range(n**2):
                if space[i][j] == info[k][0]:
                    favorite = info[k][1:]
                    break
            cnt = 0
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if space[nx][ny] in favorite:
                        cnt += 1
            if cnt == 0:
                score += 0
            else:
                score += 10**(cnt-1)
    return score

def find_space(favorite):
    arr = []
    for i in range(n):
        for j in range(n):
            favorite_cnt, void_cnt = 0, 0
            if 0 < space[i][j]:  # 이미 자리를 정한 학생이 있는 경우
                continue
            for idx in range(4): # 현재 위치에서 4 방향 탐색
                nx, ny = i + dx[idx], j + dy[idx]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    if space[nx][ny] == 0: # 비어있는 칸
                        void_cnt += 1
                    else: # 비어있지 않은 경우
                        if space[nx][ny] in favorite: # 지금 칸에 있는 학생이 좋아하는 학생일 경우
                            favorite_cnt += 1
            arr.append([favorite_cnt, void_cnt, i, j]) # 좋아하는 학생 수 / 비어있는 칸 수
    return arr

for i, x in enumerate(info):
    st = x[0]
    favorite = [x[1], x[2], x[3], x[4]]

    arr = find_space(favorite) 
    arr.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    st_x, st_y = arr[0][2], arr[0][3]

    space[st_x][st_y] = st # 자리 배치

print(calculate_score())

"""
상어 초등학교

학생: 1~n**2번 
인접 조건: 상하좌우

1. 비어있는 칸 중 좋아하는 학생과 인접한 칸이 가장 많은 칸
2. 1이 여러 개이면, 좋아하는 학생과 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
3. 2도 여러 개이면, 행, 열 번호 작은 칸 

output: 자리 배치 후 만족도(좋아하는 학생 수에 따라 결정)의 총합
"""