import sys
from collections import deque

input = sys.stdin.readline
N, Q = map(int, input().split())
space = []
for _ in range(pow(2,N)):
    space.append(list(map(int, input().split())))
L = list(map(int, input().split()))
delta = [(0,-1), (0,1), (1,0), (-1,0)]

def rotate_90(L):
    new_space = [[0]*(pow(2,N)) for _ in range(pow(2,N))]
    for i in range(0, pow(2,N), pow(2,L)):
        for j in range(0, pow(2,N), pow(2,L)):
            for x in range(pow(2,L)):
                for y in range(pow(2,L)):
                    new_space[i+y][j + pow(2,L)-x-1] = space[i+x][j+y]
    return new_space

def search():
    cnt_ice = [[0] * pow(2,N) for _ in range(pow(2,N))]
    for i in range(pow(2,N)):
        for j in range(pow(2,N)):
            cnt = 0
            for d in delta:
                nx, ny = i + d[0], j + d[1]
                if 0 <= nx and nx < pow(2,N) and 0 <= ny and ny < pow(2,N):
                    if 0 < space[nx][ny]:
                        cnt += 1
            cnt_ice[i][j] = cnt
    
    for i in range(pow(2,N)):
        for j in range(pow(2,N)):
            if 0 < space[i][j] and cnt_ice[i][j] < 3:
                space[i][j] -= 1
            
def output():
    ice, max_ice = 0, 0
    visited = [[False] * pow(2,N) for _ in range(pow(2,N))]
    
    for i in range(pow(2,N)):
        for j in range(pow(2,N)):
            ice += space[i][j] # 남은 얼음 양 count

            if not visited[i][j] and 0 < space[i][j]:
                queue = deque([(i,j)])
                visited[i][j] = True
            else:
                continue
            
            cnt = 1
            while queue:
                x, y = queue.popleft()
                for d in delta:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx and nx < pow(2,N) and 0 <= ny and ny < pow(2,N):
                        if 0 < space[nx][ny] and visited[nx][ny] == False: 
                            queue.append([nx,ny])
                            visited[nx][ny] = True
                            cnt += 1
            max_ice = max(max_ice, cnt)
    return ice, max_ice

for i in range(Q):
    space = rotate_90(L[i]) # 부분 격자 회전
    search() # 3개 이상 인접하지 않은 칸, 얼음 양 1 감소

ret = output()
print(ret[0])
print(ret[1])