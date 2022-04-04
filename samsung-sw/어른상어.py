n, m, k = map(int, input().split())

space = []
for i in range(n):
    space.append(list(map(int, input().split())))

directions = list(map(int, input().split()))
smell_space = [[[0, 0]] * n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def updateInfo():
    for i in range(n):
        for j in range(n):
            if 1<=smell_space[i][j][1]: 
                smell_space[i][j][1] -= 1
            if space[i][j]!=0:
                smell_space[i][j] = [space[i][j], k]

def move():
    new_space = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if space[x][y] != 0:
                direction = directions[space[x][y] - 1] 
                found = False

                for idx in range(4):
                    nx = x + dx[priorities[space[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[priorities[space[x][y] - 1][direction - 1][idx] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell_space[nx][ny][1] == 0: 
           
                            directions[space[x][y] - 1] = priorities[space[x][y] - 1][direction - 1][idx]
                       
                            if new_space[nx][ny] == 0:
                                new_space[nx][ny] = space[x][y]
                            else:
                                new_space[nx][ny] = min(new_space[nx][ny], space[x][y])
                            found = True
                            break
                if found:
                    continue
     
                for idx in range(4):
                    nx = x + dx[priorities[space[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[priorities[space[x][y] - 1][direction - 1][idx] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell_space[nx][ny][0] == space[x][y]: 
                      
                            directions[space[x][y] - 1] = priorities[space[x][y] - 1][direction - 1][idx]
                            new_space[nx][ny] = space[x][y]
                            break
    return new_space

time = 0
while True:
    updateInfo() 
    new_space = move() 
    space = new_space 
    time += 1

    flag = True
    for i in range(n):
        for j in range(n):
            if space[i][j] > 1:
                flag = False
    if flag:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break