import sys

sys.stdin = open('/Users/suzykwak/Desktop/sample_input.txt')
input = sys.stdin.readline

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

cnt = 0
flag = 1
direction_cnt = 0
visited = []

def init(n, m):
    global space, cnt, visited, flag, direction_cnt
    space = []
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    flag = 1
    direction_cnt = 0

# 청소 칸: -1
def cleanSpace(space, r, c):
    global cnt
    if not visited[r][c]:
        visited[r][c] = 1
        space[r][c] = -1
        cnt += 1
    return space

def clean(space):
    # 현재 칸 청소
    global r, c, d, flag, direction_cnt, visited

    while True:
        if direction_cnt == 4:
            # 바라보는 방향 유지한 채 한칸 후진
            nd = (d + 2) % 4
            r, c = r + dx[nd], c + dy[nd]
            direction_cnt = 0
            if space[r][c] == 1:
                break
            continue
        if flag:
            space = cleanSpace(space, r, c)
            flag = 0

        # 현재 위치에서 현재 방향을 기준으로 왼쪽부터 탐색
        for i in range(4):
            nd = (d-1) % 4 # left side
            nr, nc = r + dx[nd], c + dy[nd]
            # 1. 해당 방향을 청소하지 않은 경우
            if space[nr][nc] == 0:
                direction_cnt = 0
                flag = 1
                d = nd
                r, c = nr, nc
                break
            # 2. 해당 방향을 이미 청소를 한 경우
            else:
                direction_cnt += 1
                d = nd
                break

for t in range(2):
    n, m = map(int, input().split())
    init(n, m)
    r, c, d = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(n)]
    clean(space)
    print("#{}".format(t+1), cnt)
