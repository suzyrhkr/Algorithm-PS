"""DFS 풀이"""
import sys
from collections import deque

sys.setrecursionlimit(10000) # limit 풀어주지 않으면 recursion error 발생
input = sys.stdin.readline
n, m, t = map(int, input().split()) # n: 원판의 개수 / m: 원판에 적힌 정수의 개수 / t: 원판 돌리기 횟수
board = []
for i in range(n):
    board.append(deque(list(map(int, input().split()))))
info = [list(map(int, input().split())) for _ in range(t)] # x, d, k 정보

def board_sum():
    cnt, total = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != 'x':
                cnt += 1
                total += board[i][j]
    return cnt, total 

def rotate(x, d, k):
    # x 번째 원판 d방향으로 k만큼 회전
    for i, circle in enumerate(board):
        if (i + 1) % x == 0:
            if d == 0: # 양수: 시계방향 / 음수: 반시계방향
                board[i].rotate(k)
            elif d == 1:
                board[i].rotate(-k)

dx = [0, 1, 0, -1] # 오른쪽, 아래쪽, 왼쪽, 위쪽
dy = [1, 0, -1, 0]

def dfs(i, j, number, cnt, visited):
    # 조건
    j = j % m  # j 범위 처리
    if not (0 <= i and i < n):
        return cnt# 원판 범위 넘어선 경우
    # 방문 처리
    if not visited[i][j]:
        visited[i][j] = True
        if board[i][j] == number: # 수가 같은 경우 'x' 처리
            board[i][j] = 'x'
            cnt += 1
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                cnt = dfs(nx, ny, number, cnt, visited)
    return cnt

def remove():
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'x':
                continue
            num = board[i][j]
            visited = [[False] * m for _ in range(n)]
            cnt = dfs(i, j, board[i][j], 0, visited)
            if cnt == 1:
                board[i][j] = num
            if 1 < cnt: # 지운 수가 있는 경우
                flag = True
    return flag

for idx in range(t):
    x, d, k = info[idx]
    rotate(x, d, k) # 원판 돌리기
    flag = remove() # 인접한 수 지우기
    if not flag: # 인접한 수 없는 경우
        cnt, total = board_sum()
        if cnt == 0: # zero division 처리
            break
        avg = total / cnt
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'x':
                    if board[i][j] < avg: 
                        board[i][j] += 1
                    elif avg < board[i][j]:
                        board[i][j] -= 1

ret = board_sum()
print(ret[1])

"""BFS 풀이"""
import sys
from collections import deque

input = sys.stdin.readline
n, m, t = map(int, input().split()) # n: 원판의 개수 / m: 원판에 적힌 정수의 개수 / t: 원판 돌리기 횟수
board = []
for i in range(n):
    board.append(deque(list(map(int, input().split()))))
info = [list(map(int, input().split())) for _ in range(t)] # x, d, k 정보

def board_sum():
    cnt, total = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != 'x':
                cnt += 1
                total += board[i][j]
    return cnt, total # 숫자인 개수

def rotate(x, d, k):
    # x 번째 원판 d방향으로 k만큼 회전
    for i, circle in enumerate(board):
        if (i + 1) % x == 0:
            if d == 0: # 양수: 시계방향 / 음수: 반시계방향
                board[i].rotate(k)
            elif d == 1:
                board[i].rotate(-k)

dx = [0, 1, 0, -1] # 오른쪽, 아래쪽, 왼쪽, 위쪽
dy = [1, 0, -1, 0]

def bfs(i, j, number):
    cnt = 0
    queue = [i,j]
    queue = deque([queue])
    visited = [[False]*m for _ in range(n)]
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        y = y % m
        if board[x][y] == number:
            board[x][y] = 'x'
            cnt += 1
            for idx in range(4):
                nx, ny = x + dx[idx], (y + dy[idx]) % m
                if (0 <= nx and nx < n) and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
    return cnt

def remove():
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'x':
                continue
            num = board[i][j]
            cnt = bfs(i, j, num) # bfs
            if cnt == 1:
                board[i][j] = num # 인접한 수가 없는 경우 원상 복귀
            if 1 < cnt: # 지운 수가 있는 경우
                flag = True
    return flag

answer = -1
break_check = False
for idx in range(t):
    x, d, k = info[idx]
    # 원판 돌리기
    rotate(x, d, k)
    # 인접한 수 지우기
    flag = remove()
    if not flag:
        cnt, total = board_sum()
        if cnt == 0:
            answer = total
            break
        avg = total / cnt
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'x':
                    if board[i][j] < avg: 
                        board[i][j] += 1
                    elif avg < board[i][j]:
                        board[i][j] -= 1

if break_check:
    print(answer)
else:
    _, answer = board_sum()
    print(answer)