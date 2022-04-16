'''시간초과'''
import sys, copy

input = sys.stdin.readline
m, s = map(int, input().split())
fishes = []
for _ in range(m):
    x, y, d = list(map(int, input().split()))
    fishes.append([x-1, y-1, d-1])

cp_fishes = []
shark_pos = list(map(int, input().split())) 
shark_pos = shark_pos[0]-1, shark_pos[1]-1

space, smell = [], [] 
for i in range(4):
    line_1, line_2 = [], []
    for j in range(4):
        line_1.append([])
        line_2.append([])
    space.append(line_1)
    smell.append(line_2)

fish_direction = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
shark_direction = [(-1,0), (0,-1), (1,0), (0,1)]

def fish_move(): 
    size = len(fishes)
    for _ in range(size):
        x, y, d = fishes.pop(0)
        for i in range(8):
            nx, ny = x + fish_direction[d-i][0], y + fish_direction[d-i][1]
            if (0 <= nx and nx < 4 and 0 <= ny and ny < 4) and shark_pos != [nx,ny] and not smell[nx][ny]:
                # 이동
                space[x][y].remove(d)
                space[nx][ny].append((d-i)%8)
                fishes.append([nx, ny, (d-i)%8])
                break
        else:
            fishes.append([x, y, d])

def dfs(cases, x, y, depth, path, path_fishes, visited):
    if depth == 3:
        cases.append(["".join(path), path_fishes])
        return

    for i in range(4):
        nx, ny = x + shark_direction[i][0], y + shark_direction[i][1]

        if 0 <= nx < 4 and 0 <= ny < 4:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                temp = []
                for f in space[nx][ny]:
                    temp.append(f)
                dfs(cases, nx, ny, depth+1, path+[str(i+1)], path_fishes+len(temp), visited) 
                visited[nx][ny] = False
            else:
                dfs(cases, nx, ny, depth+1, path+[str(i+1)], path_fishes, visited)
        
def shark_move(idx):
    global shark_pos
    path = []
    cases = []
    x, y = shark_pos[0], shark_pos[1]
    visited = [[0]*4 for _ in range(4)]

    dfs(cases, x,y,0,[],0,visited)
    cases.sort(key=lambda x: (-x[1], x[0]))

    x, y = shark_pos[0], shark_pos[1]
    path = list(cases[0][0])
    for i, p in enumerate(path):
        p = int(p)-1
        nx, ny = x + shark_direction[p][0], y + shark_direction[p][1]
        x, y = nx, ny
        if 0 < len(space[x][y]):
            smell[x][y].append(idx)
            space[x][y] = []
            remove_list = []
            for f in fishes:
                if [f[0],f[1]] == [x,y]:
                    remove_list.append(f)
            for r in remove_list:
                fishes.remove(r)
            
        if i == 2:
            shark_pos = [x,y]

def duplicate(idx):
    cp_fishes = copy.deepcopy(fishes)
    # 1. 모든 물고기 한 칸 이동
    fish_move()
    # 2. 상어 이동
    shark_move(idx)
    # 3. 물고기 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if idx-2 in smell[i][j]:
                smell[i][j].remove(idx-2)
    # 4. 복제 물고기 생성
    for x, y, d in cp_fishes:
        space[x][y].append(d)
        fishes.append([x,y,d])

def count_fishes():
    cnt = 0
    for i in range(4):
        for j in range(4):
            cnt += len(space[i][j])
    return cnt

# main
for x, y, d in fishes:
    space[x][y].append(d)

for i in range(s):
    duplicate(i)
    
print(count_fishes())

'''other solution'''
import sys, copy

sys.stdin = open('/Users/suzykwak/Desktop/input.txt','r')
input = sys.stdin.readline
m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
space = [[[] for _ in range(4)] for _ in range(4)]

for x, y, d in fish:
    space[x - 1][y - 1].append(d - 1)

shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]

f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    global max_eat, shark, eat
    if dep == 3:  
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visit[:]
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:  
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
                visit.pop()
            else:  
                dfs(nx, ny, dep + 1, cnt, visit)

for _ in range(s):
    eat = list()
    max_eat = -1
    # 1. 모든 물고기 복제
    temp = copy.deepcopy(space)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어이동 - 백트래킹
    dfs(shark[0], shark[1],0, 0, list())
    # 4. 냄새 사라짐 
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 2   
    # 5. 복제 마법
    for i in range(4):
        for j in range(4):
            space[i][j] += temp[i][j]

# 물고기 수 구하기 
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(space[i][j])

print(answer)