import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
king_pos = -1
answer = 0
space = []

def init(r, c):
    global space, king_pos, answer
    king_pos = -1
    space = [[[] for _ in range(c)] for _ in range(r)]
    answer = 0

def check_range(i, j):
    if (0 <= i < r and 0 <= j < c):
        return True
    else:
        return False

def get(king_pos):
    global answer
    global r, c
    for i in range(r):
        if space[i][king_pos]:
            shark = space[i][king_pos][0]
            _, _, size = shark
            answer += size
            space[i][king_pos] = [] # 상어 잡음
            break

def move():
    global space
    new_space = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if space[i][j]:
                cnt = 0
                sx, sy = i, j
                s, d, z = space[i][j].pop() # 속력 방향 크기
                while cnt < s:
                    nx, ny = sx + dx[d], sy + dy[d]
                    if check_range(nx, ny): # 갈 수 있는 경우 한칸 이동
                        sx, sy = nx, ny
                    else: # 갈 수 없는 경우 방향 바꾸고 한칸 이동
                        d ^= 1
                        sx, sy = sx + dx[d], sy + dy[d]
                    cnt += 1
                new_space[sx][sy].append([s, d, z])
    space = new_space

def clean():
    for i in range(r):
        for j in range(c):
            if 1 < len(space[i][j]):
                max_size = 0
                tmp = []
                for s, d, z in space[i][j]:
                    if max_size < z:
                        max_size = z
                        tmp = [[s, d, z]]
                space[i][j] = tmp
    return

for test_case in range(1, 5):
    r, c, m = map(int, input().split())
    init(r, c)
    for _ in range(m):
        sr, sc, s, d, z = map(int, input().split())
        space[sr - 1][sc - 1] = [[s, d - 1, z]]  # 속력, 방향, 크기

    for _ in range(c):
        # 1. 낚시왕 한 칸 이동
        king_pos += 1
        # 2. 상어 잡기
        get(king_pos)
        # 3. 상어 이동
        move()
        # 상어 정리
        clean()

    print("#{}".format(test_case), answer)
