import sys

input = sys.stdin.readline
n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
ds = [list(map(int, input().split())) for _ in range(m)]

ball = [0, 0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark_x, shark_y = n//2, n//2 # 상어 위치

def fill_space(s):
    dx = [0, 1, 0, -1] #하우상좌
    dy = [-1, 0, 1, 0]

    for _ in range(s):
        move_cnt, dist, direction = 0, 1, 0
        x, y = n//2, n//2
        flag = False
        while [x,y] != [0,-1]:
            for i in range(dist):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if not flag and space[x][y] == 0 and [x,y]!=[n//2, n//2]:
                    flag = True
                if flag: # 상어 자리가 아닌, 맨 처음 빈 칸을 발견한 경우
                    if [nx,ny] == [0,-1]:
                        space[x][y] = 0
                    else:
                        space[x][y] = space[nx][ny] 
                x, y = nx, ny 
            move_cnt += 1
            direction = (direction + 1) % 4
            if move_cnt == 2:
                dist += 1
                move_cnt = 0
 
def boom():
    dx = [0, 1, 0, -1] #하우상좌
    dy = [-1, 0, 1, 0]
    flag = False # 더이상 폭발할 구슬이 없는 경우 True

    while not flag:
        boom_list = []
        boom_cnt = 0
        move_cnt, dist, direction = 0, 1, 0
        x, y = n//2, n//2

        while [x,y] != [0,-1]:
            for i in range(dist):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 다음 칸이 연속인 수이면 boom_list에 담기
                if space[x][y] == space[nx][ny]:
                    if 0 < space[x][y]:
                        boom_list.append([x,y,space[x][y]]) # x, y좌표와 구슬 번호
                else:
                    if boom_list:
                        if boom_list[0][2] == space[x][y]: 
                            if 0 < space[x][y]:
                                boom_list.append([x,y,space[x][y]])
                    if len(boom_list) < 4:
                       boom_list = []
                    else:
                        for pos_x, pos_y, num in boom_list:
                            space[pos_x][pos_y] = 0
                            ball[num-1] += 1
                            boom_cnt += 1
                        boom_list = []
                x, y = nx, ny 
            move_cnt += 1
            direction = (direction + 1) % 4
            if move_cnt == 2:
                dist += 1
                move_cnt = 0 
        if not boom_cnt:
            flag = True
        # 폭발한 부분 채우기
        fill_space(boom_cnt)

def change():
    global space
    new_space = [[0]*n for _ in range(n)]
    new_list = []
    dx = [0, 1, 0, -1] #하우상좌
    dy = [-1, 0, 1, 0]

    move_cnt, dist, direction = 0, 1, 0
    x, y = n//2, n//2
    group = [0,0] # group_cnt, group_num 
    while [x,y] != [0,-1]:
        for i in range(dist):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if space[x][y] == space[nx][ny]:
                if 0 < space[x][y]:
                    group[0] += 1
                    group[1] = space[x][y]
            else:
                if group != [0,0]:
                    if group[1] == space[x][y]:
                        if 0 < space[x][y]:
                            group[0] += 1
                            group[1] = space[x][y]
                else:
                    if 0 < space[x][y]:
                        group[0] += 1
                        group[1] = space[x][y]
                if 0 < group[1]:
                    new_list.extend([group[0], group[1]])
                    group = [0,0]
            x, y = nx, ny 
        move_cnt += 1
        direction = (direction + 1) % 4
        if move_cnt == 2:
            dist += 1
            move_cnt = 0
    new_list.extend([group[0], group[1]])

    # 변화한 space 생성
    move_cnt, dist, direction = 0, 1, 0
    x, y = n//2, n//2
    flag = False
    idx = 0

    while [x,y] != [0,-1]:
        for i in range(dist):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if [x,y] != [n//2, n//2]:
                new_space[x][y] = new_list[idx]
                idx += 1
                if len(new_list) == idx:
                    space = new_space
                    return
            x, y = nx, ny 
        move_cnt += 1
        direction = (direction + 1) % 4
        if move_cnt == 2:
            dist += 1
            move_cnt = 0           
    space = new_space

def blizard(d,s):
    for i in range(1,s+1):
        nx = shark_x + (i * dx[d-1])
        ny = shark_y + (i * dy[d-1])
        space[nx][ny] = 0 
    fill_space(s) 
    boom()
    change()
    
# main
for i in range(m):
    blizard(ds[i][0], ds[i][1])
  
print(ball[0] + 2*ball[1] + 3*ball[2])