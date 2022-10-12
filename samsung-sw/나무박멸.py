import sys

input = sys.stdin.readline

killer = []
ans = 0

def init(n):
    global killer, ans
    killer = [[0] * n for _ in range(n)]
    ans = 0

def check(i, j):
    return True if (0 <= i < n and 0 <= j < n) else False

def grow():
    new_sp = [[0]*n for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(n):
            if 0 < space[i][j]: # 나무가 있는 칸의 경우
                cnt = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if check(nx, ny) and 0 < space[nx][ny]:
                        cnt += 1
                new_sp[i][j] += cnt

    for i in range(n):
        for j in range(n):
            space[i][j] += new_sp[i][j]

def spread():
    new_sp = [[0] * n for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(n):
            if 0 < space[i][j]:
                cnt = 0
                candidates = []
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if check(nx, ny):
                        # 빈 칸이고, 제초제도 없는 경우
                        if space[nx][ny] == 0 and killer[nx][ny] == 0:
                            cnt += 1
                            candidates.append([nx, ny])
                for x, y in candidates:
                    new_sp[x][y] += (space[i][j] // cnt)

    for i in range(n):
        for j in range(n):
            space[i][j] += new_sp[i][j]

def bfs(i, j):
    cnt = 0
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    # 현재 칸 처리
    pos = [[i, j]]
    cnt += space[i][j]

    # 사방 처리
    for d in range(4):
        nx, ny = i, j
        for t in range(k):
            nx, ny = nx + dx[d], ny + dy[d]
            if check(nx, ny):
                pos.append([nx, ny])
                if space[nx][ny] != -1: # 벽이 아닌 경우
                    cnt += space[nx][ny]
                if space[nx][ny] <= 0:
                    break
            else:
                break
    return cnt, pos

def kill():
    global ans
    # 제초제를 뿌릴 때 가장 많이 박멸되는 칸 찾기
    max_val = 0
    max_pos = [-1, -1]
    max_path = []

    for i in range(n):
        for j in range(n):
            if 0 < space[i][j]: # 나무가 있는 경우
                cnt, path = bfs(i, j)
                if max_val < cnt:
                    max_val = cnt
                    max_pos = [i, j]
                    max_path = path

    # 제초제 뿌리기
    for x, y in max_path:
        killer[x][y] = c
        if 0 < space[x][y]:
            space[x][y] = 0
    # 박멸한 나무의 수 더하기
    ans += max_val

def clean_killer():
    for i in range(n):
        for j in range(n):
            if 0 < killer[i][j]:
                killer[i][j] -= 1

for n_case in range(3):
    n, m, k, c = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(n)]
    init(n)
    for _ in range(m):
        grow()
        spread()
        clean_killer()
        kill()
    print(ans)
