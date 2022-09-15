import sys

input = sys.stdin.readline
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 보드 색
info = [[[] for _ in range(n)] for _ in range(n)] # 모든 말의 위치, 방향 정보
chess = {} # 말의 현재 위치
turn = 0

# 우 좌 상 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    x, y, d = map(int, input().split())
    chess[i+1] = [x-1, y-1, d-1]
    info[x-1][y-1].append(i+1)

def move():
    global chess, info
    # 1~k번 말 이동
    for i in range(1, k+1):
        cx, cy, cd = chess[i]
        nx, ny = cx + dx[cd], cy + dy[cd]
        # 이동할 칸이 파란 색이거나 범위를 벗어난 경우
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            cd ^= 1  # 이동 방향 변경
            nx, ny = cx + dx[cd], cy + dy[cd]
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                nx, ny = cx, cy

        chess[i] = [nx, ny, cd]
        if [nx, ny] == [cx, cy]:
            continue

        cidx = info[cx][cy].index(i)
        candidates = info[cx][cy][cidx:]

        for c in candidates:
            chess[c][0] = nx
            chess[c][1] = ny

        # 말 이동
        if board[nx][ny] == 0: # white
            info[nx][ny] += candidates
        elif board[nx][ny] == 1: # red
            info[nx][ny] += candidates[::-1]

        info[cx][cy] = info[cx][cy][:cidx]
        if 4 <= len(info[nx][ny]):
            return -1
    return 0

while True:
    turn += 1
    if 1000 < turn:
        turn = -1
        break

    ret = move()
    if ret == -1:
        break

print(turn)

'''
말의 개수 k개 - 원판모양, 겹치기 가능
체스판 - 흰색, 빨간색, 파란색
    0은 흰색, 1은 빨간색, 2는 파란색

구하는 것: turn의 수
'''