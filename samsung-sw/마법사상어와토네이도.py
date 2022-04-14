import sys
import math

input = sys.stdin.readline
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

coord = [(-2,0), 
    (-1,-1), (-1,0), (-1,1), 
    (0,-2), (0,-1), 
    (1,-1), (1,0), (1,1),
    (2,0)]
percentage = [0.02, 0.1, 0.07, 0.01, 0.05, None, 0.1, 0.07, 0.01, 0.02]

base = [[0]*5 for _ in range(5)]
x_end, y_end = 2, 2
out = 0

for c, p in zip(coord, percentage):
    nx = x_end + c[0]
    ny = y_end + c[1]
    base[nx][ny] = p

def rotate_base(direction):
    origin = base
    rotated = []
    for _ in range(direction):
        rotated = [[0]*5 for _ in range(5)] 
        for i in range(5):
            for j in range(5):
                rotated[5-j-1][i] = origin[i][j]
        origin = rotated
    return origin

def calculate(direction, x, y):
    global out
    rotated = rotate_base(direction)
 
    current = space[x][y]
    difused = 0

    for i in range(-2,3):
        for j in range(-2,3):
            nx, ny = x + i, y + j
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if rotated[i+2][j+2]:
                    value = math.floor(rotated[i+2][j+2] * space[x][y])
                    space[nx][ny] += value
                    difused += value
            else:
                if rotated[i+2][j+2]:
                    value = math.floor(rotated[i+2][j+2] * space[x][y])
                    out += value
                    difused += value

    # alpha 값
    nx, ny = x + directions[direction][0], y + directions[direction][1]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
        space[nx][ny] += current - difused
    else:
        out += current - difused
    space[x][y] = 0

directions = [(0,-1), (1,0), (0,1), (-1,0)] 

def tornado():
    x, y = (n//2), (n//2)
    move_cnt, dist, d = 0, 1, 0
    # (1,1)에 도착하면 소멸
    while [x,y]!=[0,-1]:
        for _ in range(dist):
            nx, ny = x + directions[d][0], y + directions[d][1]
            calculate(d, nx, ny)
            x, y = nx, ny
        
        move_cnt += 1
        if move_cnt == 2:
            dist += 1
            move_cnt = 0
        d = (d+1) % 4

tornado()
print(out)