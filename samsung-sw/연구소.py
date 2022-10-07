import sys
from itertools import combinations
import copy

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(n, m, x, y):
    if (0 <= x < n and 0 <= y < m):
        return True
    else:
        return False

def init():
    global virus_pos, wall_candidates, n_walls, answer
    virus_pos = []
    wall_candidates = []
    n_walls = 0
    answer = 0

def spread_virus(space, virus_pos, n, m):
    cnt = 0
    for vx, vy in virus_pos:
        cnt += 1
        queue = [(vx, vy)]
        while queue:
            x, y = queue.pop(0)
            # 상하좌우 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not check(n, m, nx, ny):  # 위치가 공간을 벗어난 경우
                    continue
                # 빈 공간 큐에 추가
                if space[nx][ny] == 0:
                    queue.append((nx, ny))
                    space[nx][ny] = 2
                    cnt += 1
    return cnt

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
init()

for i in range(n):
    for j in range(m):
        if space[i][j] == 0:
            wall_candidates.append((i, j))
        elif space[i][j] == 1:
            n_walls += 1
        elif space[i][j] == 2:
            virus_pos.append((i, j))

wall_combinations = list(combinations(wall_candidates, 3))

for combination in wall_combinations:
    space_cp = copy.deepcopy(space)
    for wx, wy in combination:
        space_cp[wx][wy] = 1 # 조합 자리 -> 벽으로 대체

    # 바이러스 퍼짐
    cnt = spread_virus(space_cp, virus_pos, n, m)
    answer = max(answer, n*m - (n_walls + cnt + 3))

print(answer)