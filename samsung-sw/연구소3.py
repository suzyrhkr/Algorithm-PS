import copy
import sys
from itertools import combinations

input = sys.stdin.readline

INF = float('inf')
virus_pos = []
n_walls = 0
n_virus = 0
min_t = INF
flag = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def init():
    global virus_pos, n_walls, n_virus, min_t, flag, virus_combinations, space
    virus_pos = []
    n_walls = 0
    n_virus = 0
    min_t = INF
    flag = 0
    virus_combinations = []
    space = []

def check(x, y, n):
    if (0 <= x < n and 0 <= y < n):
        return True
    else:
        return False

def isEmpty(space, n):
    for i in range(n):
        for j in range(n):
            if space[i][j] == 'o':
                return False
    return True

def bfs(space, combination):
    queue = []
    t = 0
    cnt = 0
    # 바이러스 m개 활성화
    # 비활성 바이러스 *, 활성 바이러스 0
    for i, j in combination:
        space[i][j] = 0 # 바이러스 활성화
        queue.append((i, j))
    # 'o'인 위치만 바이러스 전파 가능
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not check(nx, ny, n): # 범위 벗어난 경우
                continue
            if space[nx][ny] == 'o':
                cnt += 1
                queue.append((nx, ny))
                space[nx][ny] = space[x][y] + 1
                t = max(t, space[nx][ny])
            elif space[nx][ny] == '*': # 비활성 바이러스인 경우
                queue.append((nx, ny))
                space[nx][ny] = space[x][y] + 1 # **

    return t if isEmpty(space, n) else INF

for n_case in range(1, 8):
    init()
    n, m = map(int, input().split())

    for i in range(n):
        input_row = list(map(int, input().split()))
        row = []
        for j in range(n):
            if input_row[j] == 0:
                row.append('o')
            elif input_row[j] == 1:
                row.append('-')
                n_walls += 1
            elif input_row[j] == 2:
                row.append('*')
                virus_pos.append((i, j))
                n_virus += 1
        space.append(row)

    # 바이러스 조합 생성
    virus_combinations = list(combinations(virus_pos, m))

    for combination in virus_combinations:
        space_cp = copy.deepcopy(space)
        ret = bfs(space_cp, combination)
        if ret != INF:
            min_t = min(min_t, ret)
            flag = 1

    if flag:
        print("#{}".format(n_case), min_t)
    else:
        print("#{}".format(n_case), -1)