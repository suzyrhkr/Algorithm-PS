import sys
from collections import deque
import math

input = sys.stdin.readline
n, m, k = list(map(int, input().split()))
fireball_info = [list(map(int, input().split())) for _ in range(m)]

space = [[[] for _ in range(n)] for _ in range(n)]
fireball = []
for f in fireball_info:
    r, c, m, s, d = f[0]-1, f[1]-1, f[2], f[3], f[4]
    fireball.append([r, c, m, s, d])
fireball = deque(fireball)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def movement():
    length = len(fireball)
    while fireball:
        x, y, m, s, d = fireball.popleft()
        nx, ny = (x + s * dx[d]) % n, (y + s * dy[d]) % n
        space[nx][ny].append([m,s,d])

def after_movement():
    for i in range(n):
        for j in range(n):
            length = len(space[i][j])
            # 2 개 이상 파이어볼 있는 칸 
            if 1 < length:
                sum_m, sum_s = 0, 0
                odd, even = 0, 0
                while space[i][j]:
                    m, s, d = space[i][j].pop(0)
                    sum_m += m
                    sum_s += s
                    if (d % 2) != 0:
                        odd += 1
                    else:
                        even += 1

                new_m = math.floor(sum_m/5)

                if new_m == 0:
                    continue

                new_s = math.floor(sum_s/(length))
        
                if length in [odd, even]:
                    new_direction = [0,2,4,6]
                else:
                    new_direction = [1,3,5,7]

                for new_d in new_direction:
                    fireball.append([i, j, new_m, new_s, new_d])
   
            elif len(space[i][j]) == 1:
                info = [i,j] + space[i][j].pop()
                fireball.append(info)
          
def total_mass():
    total = 0
    for f in fireball:
        total += f[2]
    return total

for i in range(k):
    movement()
    after_movement()

print(total_mass())
