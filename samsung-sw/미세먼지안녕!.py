r, c, t = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 미세먼지 확산 func
def dust():
    add_dust = [[0]*c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            # 미세먼지가 있는 경우(공기청정기 있는 칸이 아닌.)
            current_dust = space[i][j]
            difuse_dust = current_dust//5
            cnt = 0 # 확산된 방 개수 
            if 0 < space[i][j]:
                for idx in range(4):
                    nx, ny = i + dx[idx], j + dy[idx]
                    # 칸이 있는 경우 and 공기 청정기 구역이 아닌 경우
                    if (0 <= nx and nx < r and 0 <= ny and ny < c) and space[nx][ny] != -1: 
                        add_dust[nx][ny] += difuse_dust
                        cnt += 1
                space[i][j] = current_dust - (cnt * difuse_dust)

    for i in range(r):
        for j in range(c):
            space[i][j] += add_dust[i][j]
            
    return

# 공기 청정기 위치 찾기 func
def find_location():
    for i in range(r):
        if space[i][0] == -1 and space[i+1][0] == -1:
            location = [i, i+1]
    return location

# 공기 청정기 동작 func
def fresh_air(location):
    # 공기 청정기 위치
    upside, downside = location
    # 윗 방향 회전
    for i in range(upside-1, -1, -1): ## 하 이동
        space[i+1][0] = space[i][0]
    for j in range(1, c): ## 좌 이동
        space[0][j-1] = space[0][j]
    for i in range(1, upside+1): ## 상 이동
        space[i-1][c-1] = space[i][c-1]
    for j in range(c-2, 0, -1): ## 우 이동
        space[upside][j+1] = space[upside][j]

    # 아랫 방향 회전
    for i in range(downside+1, r): # 상 이동
        space[i-1][0] = space[i][0]
    for j in range(1, c): # 좌 이동
        space[r-1][j-1] = space[r-1][j] 
    for i in range(r-2, downside-1, -1): # 하 이동
        space[i+1][c-1] = space[i][c-1]
    for j in range(c-2, 0, -1):
        space[downside][j+1] = space[downside][j]

    # 공기 청정기 위치에 -1 다시 입력
    space[upside][0], space[downside][0] = -1, -1
    # upside, downside의 공기 정화 부분
    space[upside][1] = 0
    space[downside][1] = 0

    return

def remaining_dust():
    dust_sum = 0
    for i in range(r):
        for j in range(c):  
            if space[i][j] !=- 1:
                dust_sum += space[i][j]
    return dust_sum

# main
ret = find_location()

for i in range(t):
    dust()
    fresh_air(ret)

print(remaining_dust())